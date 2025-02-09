from django.db import models
from suppliers.models import Supplier

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=255, default='Default description')

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, default=0.00, decimal_places=3)
    stock_quantity = models.IntegerField()
    reorder_level = models.IntegerField()
    supplier_details = models.ManyToManyField(Supplier)

    def __str__(self):
        return self.name


    def __str__(self):
        return self.name