from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginview, name='login'),
    path('signup/', views.signupview, name='signup'),
    path('dashboard/', views.dashboardview, name='dashboard'),
    path('logout/', views.logoutview, name='logout'),
]
