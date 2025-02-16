from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from customers.models import Customer

class TestOrder(APITestCase):
    def setUp(self):
        Customer.objects.create(name = "TestCustomer1") 
        Customer.objects.create(name = "testCustomer2")
        self.user = User.objects.create(
            username = "admin",
            password =  "admin"
        )

    def test_get_customer(self):
        response = self.client.get('/api/customer/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.data),2)

    def test_post_customer_without_login(self):
        data = {
            "name":"customer"
        } 

        response = self.client.post('/customers/api/customer',data = data)  
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def  test_post_customer(self):
        data = {
            "name":"customer"
        }  
        self.client.force_authenticate(self.user)
        response = self.client.post('/customers/api/customer', data=data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)
        self.assertAlmostEqual(response.json()['message'],"Customer Added Successfully") 