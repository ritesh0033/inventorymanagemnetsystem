from rest_framework.test import APITestCase
from rest_framework import status
from suppliers.models import Supplier
from django.urls import reverse


class SupplierTest(APITestCase):
    def setUp(self):

        self.supplier = Supplier.objects.create(
            supplier_id=1,
            name="Supplier A",
            address="123 Test Street",
            contact_info="9876543210",
            is_active=True
        )


        self.url = reverse('supplier-list-create-api') 

        
        self.new_supplier_data = {
            'supplier_id': 2,
            'name': "Supplier B",
            'address': "456 Another St",
            'contact_info': "1234567890",
            'is_active': True
        }

    def test_get_suppliers(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_supplier(self):
        response = self.client.post(self.url, data=self.new_supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.json()['message'], "Supplier addes Sucessfully")

    def test_post_supplier_without_authentication(self):
        self.client.logout()  
        response = self.client.post(self.url, data=self.new_supplier_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
