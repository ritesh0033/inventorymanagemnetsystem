from django.contrib import admin
from .models import Category,Product
from djangoql.admin import DjangoQLSearchMixin

@admin.register(Category)
class  CategoryAmin(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display = ['name']


@admin.register(Product)
class Product(DjangoQLSearchMixin,admin.ModelAdmin):
    list_display = ['product_id','name','category']    
