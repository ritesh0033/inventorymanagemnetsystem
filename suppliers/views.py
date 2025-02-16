from django.shortcuts import render
from .models import Supplier
from .forms import SupplierForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView,DeleteView,CreateView
from django.core.paginator import Paginator

def suppliers_list(request): 
    suppliers_list = Supplier.objects.all()
    paginator  = Paginator(suppliers_list,25)
    page_number = request.GET.get('page')
    suppliers = paginator.get_page(page_number)

    return render (request,"suppliers/suppliers_list.html",{'suppliers':suppliers})



class SupplierAdd(LoginRequiredMixin,CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_create.html"
    success_url = '/orders/list/'


 
class SupplierUpdate(LoginRequiredMixin,UpdateView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_update.html"
    success_url = '/suppliers/list/'   


class SupplierDelete(LoginRequiredMixin,DeleteView):
    model = Supplier
    form_class = SupplierForm
    template_name = "suppliers/suppliers_delete.html"
    success_url = '/suppliers/list/'    