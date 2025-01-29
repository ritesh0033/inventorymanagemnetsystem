from django.db import models



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    contact_info = models.TextField(max_length=20)
    address = models.CharField(max_length=100)

   
    def __str__(self):
        return self.name