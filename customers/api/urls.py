from django.urls import path
from .views import CustomerView, CustomerRetrieveUpdateDestroyAPIView

urlpatterns = [
    
    path('', CustomerView.as_view(), name='customer-list-create-api'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer-retrieve-update-destroy-api'),
]