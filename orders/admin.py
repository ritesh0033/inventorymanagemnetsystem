from django.contrib import admin
from .models import Order
from djangoql.admin import DjangoQLSearchMixin


@admin.register(Order)
class OrderAdmin(DjangoQLSearchMixin, admin.ModelAdmin):
    search_fields = ['order_details__product_name']  
    list_display = ['order_id', 'customer', 'order_date', 'status',]  
