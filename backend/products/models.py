from django.db import models
from branches.models import Company


class Product(models.Model):
    TYPE_CHOICES = [
        ('Mobile',          'Mobile'),
        ('Laptop',          'Laptop'),
        ('LED TV',          'LED TV'),
        ('Washing Machine', 'Washing Machine'),
        ('Refrigerator',    'Refrigerator'),
        ('Mixi',            'Mixi'),
        ('Other',           'Other'),
    ]

    product_id = models.CharField(max_length=20, unique=True)
    name       = models.CharField(max_length=255)
    type       = models.CharField(max_length=50, choices=TYPE_CHOICES)
    image      = models.ImageField(upload_to='products/', null=True, blank=True)
    details    = models.TextField()
    price      = models.DecimalField(max_digits=10, decimal_places=2)
    discount   = models.DecimalField(max_digits=5,  decimal_places=2, default=0)
    stock      = models.IntegerField(default=0)
    company    = models.ForeignKey(
        Company, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='products'
    )
    is_active  = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.product_id} – {self.name}"

    @property
    def discounted_price(self):
        return round(float(self.price) * (1 - float(self.discount) / 100), 2)

    @property
    def image_url(self):
        return self.image.url if self.image else None
