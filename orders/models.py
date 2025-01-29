from django.db import models
from django.utils.timezone import now
from customers.models import Customer
from product.models import Product


class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "Pending"
        PROCESSING = "Processing"
        SHIPPED = "Shipped"
        DELIVERED = "Delivered"
        CANCELLED = "Cancelled"

    order_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField(default=now, blank=True)
    status = models.CharField(max_length=100, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    order_details = models.ManyToManyField(Product)  

    def __str__(self):
        return f"Order {self.order_id} - {self.status}"


