from django.db import models

class Company(models.Model):
    company_id      = models.CharField(max_length=20, unique=True)
    name            = models.CharField(max_length=255)
    image           = models.ImageField(upload_to='companies/', null=True, blank=True)
    details         = models.TextField()
    address         = models.TextField()
    contact_number  = models.CharField(max_length=20)
    toll_free_number= models.CharField(max_length=20, blank=True)
    is_active       = models.BooleanField(default=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'companies'
        ordering = ['name']

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        return self.image.url if self.image else None
