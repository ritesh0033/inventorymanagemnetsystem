from django.urls import path
from .views import customers_list, CustomerAdd, CustomerUpdate, CustomerDelete

urlpatterns = [
    path('list/', customers_list, name='customers_list'),  
    path('add/', CustomerAdd.as_view(), name='customers_add'),  
    path('update/<int:pk>/', CustomerUpdate.as_view(), name='customers_update'),  
    path('delete/<int:pk>/', CustomerDelete.as_view(), name='customers_delete'),  
]

