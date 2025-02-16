from django.shortcuts import render
from .models import User
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserForm
from django.core.paginator import Paginator

def users_list(request):
    users_list = User.objects.all()
    paginator = Paginator(users_list,25)
    page_number = request.GET.get('page')
    users = paginator.get_page(page_number)
    return render(request, "users/users_list.html", {'users': users})

class UserAdd(LoginRequiredMixin, CreateView):
    model = User
    form_class = UserForm
    template_name = "users/users_create.html"
    success_url = '/users/list/'

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = "users/users_update.html"
    success_url = '/users/list/'

class UserDelete(LoginRequiredMixin, DeleteView):
    model = User
    form_class = UserForm
    template_name = "users/users_delete.html"
    success_url = '/users/list/'
