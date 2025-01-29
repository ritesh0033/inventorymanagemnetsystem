from django.urls import path
from .views import CategoryView, CategoryRetrieveUpdateDestroy, ProductView,ProductRetrieveUpdateDestroy


urlpatterns = [
    # Category Endpoints
    path('categories/', CategoryView.as_view(), name='category-list-create-api'),
    path('categories/<int:pk>/', CategoryRetrieveUpdateDestroy.as_view(), name='category-retrieve-update-destroy-api'),

    # Product Endpoints
    path('products/', ProductView.as_view(), name='product-list-create-api'),
    path('products/<int:pk>/',ProductRetrieveUpdateDestroy.as_view(), name='product-retrieve-update-destroy-api'),
]

