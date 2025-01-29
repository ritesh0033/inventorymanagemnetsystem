from django.contrib import admin
from .models import Supplier
from djangoql.admin import DjangoQLSearchMixin

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
 pass    

