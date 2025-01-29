from django.contrib import admin
from .models import Customer
from djangoql.admin import DjangoQLSearchMixin

@admin.register(Customer)

class CustomerAdmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display = ['name'] 
