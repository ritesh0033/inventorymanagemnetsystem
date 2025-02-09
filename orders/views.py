from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Order
from .forms import OrdersForm

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

class OrderAdd(LoginRequiredMixin, CreateView):
    model = Order
    form_class = OrdersForm
    template_name = "orders/orders_create.html"
    success_url = reverse_lazy('order_list')

class OrderUpdate(LoginRequiredMixin, UpdateView):
    model = Order
    form_class = OrdersForm
    template_name = "orders/orders_update.html"
    success_url = reverse_lazy('order_list')

class OrderDelete(LoginRequiredMixin, DeleteView):
    model = Order
    template_name = "orders/orders_delete.html"
    success_url = reverse_lazy('order_list')
