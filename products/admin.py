from django.contrib import admin
from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["title", "description", "price"]
    ordering = ["-price"]

# # Register your models here.
# admin.site.register(Product, ProductAdmin)

