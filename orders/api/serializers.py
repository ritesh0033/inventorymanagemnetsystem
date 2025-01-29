from rest_framework import serializers
from orders.models import Order
from customers.api.serializers import CustomerSerializer
from product.api.serializers import ProductSerializer

class OrderSerializer(serializers.ModelSerializer):
    
    customer = CustomerSerializer()
    order_details = ProductSerializer(many=True)
  

    class Meta:
        model = Order
        fields = ['order_id', 'customer', 'order_date', 'status', 'order_details']
