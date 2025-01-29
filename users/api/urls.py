from django.urls import path
from .views import RoleView,RoleRetrieveUpdateDestroy,UserView,UserRetrieveUpdateDestroy

urlpatterns = [
    path('roles/',RoleView.as_view(),name = 'role-list-create'),
    path('roles/<int:pk>/',RoleRetrieveUpdateDestroy.as_view(),name = 'role-retrieve-update-destroy'),
    path('users/',UserView.as_view(),name = 'user-list-create'),
    path('user/<int:pk>/',UserRetrieveUpdateDestroy.as_view(),name ='user-retrieve-update-destroy'),

]