from django.shortcuts import render
from .models import Product
from django.views.generic import UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ProductForm


def products_list(request):
    products = Product.objects.all()
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



