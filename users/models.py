from django.db import models

class Role(models.Model):
    class RoleChoices(models.TextChoices):
        ADMIN = 'admin', 'Admin'
        STAFF = 'staff', 'Staff'
        USER = 'user', 'User'
    role_name = models.CharField(max_length=100, choices=RoleChoices.choices, default=RoleChoices.USER)
    description = models.TextField(max_length=255, default='Default description', blank=True)
    def __str__(self):
        return self.role_name


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, default='', blank=True,unique=True)
    password = models.CharField(max_length=100)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1) 

    def __str__(self):
        return self.name
