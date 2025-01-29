from rest_framework import serializers
from suppliers.models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_id','name','address','contact_info','is_active']