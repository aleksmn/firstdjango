from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True, default="No description")
    price = models.DecimalField(max_digits=10, decimal_places=2) # 99 999 999.99
    featured = models.BooleanField(default=False)
