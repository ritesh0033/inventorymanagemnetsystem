from django.urls import path
from .views import SupplierView,SupplierRetrieveUpdateDestroy


urlpatterns = [
    path('suppliers',SupplierView.as_view(),name = 'supplier-list-create-api'),
    path('suppliers/<int:pk>/',SupplierRetrieveUpdateDestroy.as_view(),name = 'supplier-retrieve-update-destroy')
]