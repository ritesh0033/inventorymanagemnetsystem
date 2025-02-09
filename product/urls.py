from django.urls import path
from .views import products_list, AddProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('list/', products_list, name='products_list'),  
    path('add/', AddProduct.as_view(), name='product_add'),
    path('delete/<int:pk>/', DeleteProduct.as_view(), name='product_delete'),  
    path('update/<int:pk>/', UpdateProduct.as_view(), name='product_update'),  
]
