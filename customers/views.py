from django.shortcuts import render
from .models import Customer
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CustomerForm
from django.core.paginator import Paginator


def customers_list(request):
    customers_list = Customer.objects.all()
    paginator = Paginator(customers_list,25)
    page_number = request.GET.get('page')
    customers = paginator.get_page(page_number)
   
    return render(request, 'customers/customers_list.html', {'customers': customers})


class CustomerAdd(LoginRequiredMixin,CreateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers_create.html"
    success_url = '/customers/list/'
class CustomerUpdate(LoginRequiredMixin,UpdateView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers_update.html"
    success_url = '/customers/list/'

class CustomerDelete(LoginRequiredMixin,DeleteView):
    model = Customer
    form_class = CustomerForm
    template_name = "customers/customers_delete.html"
    success_url = '/customers/list/'

