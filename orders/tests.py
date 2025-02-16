from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from orders.models import Order
from customers.models import Customer

User = get_user_model()

class OrderAPITestCase(APITestCase):
    def setUp(self):
        

        self.customer = Customer.objects.create(
            name='Test Customer'
        )
        
        
        self.order = Order.objects.create(
            customer=self.customer,
            order_date='2025-02-16',
            status='Pending'
        )

        
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    def test_get_orders_without_login(self):
        response = self.client.get('orders/api/order/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        

    def test_post_order_without_login(self):

        data = {
            "customer": self.customer.id,
            "order_date": "2025-02-17",
            "status": "Confirmed"
        }
        response = self.client.post('orders/api/order/', data=data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_post_order(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "customer": self.customer.id,
            "order_date": "2025-02-17",
            "status": "Confirmed"
        }
        response = self.client.post('orders/api/order/', data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['message'], "Order Added Successfully")
