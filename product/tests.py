from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from product.models import Category, Product
from django.contrib.auth.models import User


class ProductTests(TestCase):
    def setUp(self):
        
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        
        self.category = Category.objects.create(name='Electronics')

        self.product_data = {
            'name': 'Laptop',
            'description': 'A powerful laptop',
            'price': 999.99,
            'stock_quantity': 10,
            'reorder_level': 5,
            'category': self.category  
        }
        self.product = Product.objects.create(**self.product_data)

    def test_create_product(self):
        response = self.client.post('/api/products/', data=self.product_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['message'], 'Product added successfully')

    def test_get_product(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  

  
   
