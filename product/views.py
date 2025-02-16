from django.shortcuts import render
from .models import Product
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm
from django.core.paginator import Paginator


def products_list(request):
    product_list = Product.objects.all()
    paginator = Paginator(product_list,25)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    return render(request,'product/product_list.html',{'products':products})


class AddProduct(LoginRequiredMixin,CreateView):
     model = Product
     form_class = ProductForm
     template_name = "product/product_create.html"
     success_url = '/product/list'

class UpdateProduct(LoginRequiredMixin,UpdateView):
     model = Product
     form_class = ProductForm
     template_name = "product/product_update.html"
     success_url = '/product/list'


class DeleteProduct(LoginRequiredMixin,DeleteView):
     model = Product
     form_class = ProductForm
     template_name = "product/product_delete.html"
     success_url = '/product/list'



