from product.models import Product, Category
from rest_framework import serializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'  


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)  

    class Meta:  
        model = Product
        fields = [
            'product_id',
            'name',
            'description',
            'price',
            'stock_quantity',
            'reorder_level',
            'category',  
        ]

    def to_representation(self, instance):
        
        data = super().to_representation(instance)
        data['price'] = f"${instance.price:.2f}"  
        return data


    