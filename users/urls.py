from django.urls import path
from .views import users_list, UserAdd, UserUpdate, UserDelete

urlpatterns = [
    path('list/', users_list, name='users_list'),  # Path for listing users
    path('add/', UserAdd.as_view(), name='users_add'),  # Path for adding a user
    path('update/<int:pk>/', UserUpdate.as_view(), name='users_update'),  # Path for updating a user
    path('delete/<int:pk>/', UserDelete.as_view(), name='users_delete'),  # Path for deleting a user
]
