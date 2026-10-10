from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('role', 'admin')
        return self.create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    ROLE_CHOICES = [('admin','Admin'),('customer','Customer')]
    GENDER_CHOICES = [('Male','Male'),('Female','Female'),('Other','Other')]
    AGE_CHOICES = [('18-25','18-25'),('26-35','26-35'),('36-45','36-45'),('46-60','46-60'),('60+','60+')]

    username       = models.CharField(max_length=150, unique=True)
    email          = models.EmailField(unique=True)
    full_name      = models.CharField(max_length=255, blank=True)
    address        = models.TextField(blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    gender         = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    age_range      = models.CharField(max_length=10, choices=AGE_CHOICES, blank=True)
    role           = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    is_active      = models.BooleanField(default=True)
    is_staff       = models.BooleanField(default=False)
    date_joined    = models.DateTimeField(auto_now_add=True)
    updated_at     = models.DateTimeField(auto_now=True)

    objects = UserManager()
    USERNAME_FIELD  = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f"{self.username} ({self.role})"
