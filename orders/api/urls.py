from django.urls import path
from .views import OrderView,OrderRetrieveUpdateDestroy

urlpatterns = [
    path('orders/',OrderView.as_view(),name = 'order-list-create-api'),
    path('oreders/<int:pk>',OrderRetrieveUpdateDestroy.as_view,name = 'order-retrieve-update-destroy-api'),
]