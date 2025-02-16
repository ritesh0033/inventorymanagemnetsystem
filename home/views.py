from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSignupForm
from django.contrib.auth.hashers import make_password
from orders.models import Order
from django.db.models import Count

def loginview(request):
    if request.method == "POST":
        username_or_email = request.POST.get("username_or_email")  
        password = request.POST.get("password")

        if not username_or_email or not password:
            messages.error(request, "Username/Email and password are required.")
            return redirect("login")
        if "@" in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
                username = user.username 
            except User.DoesNotExist:
                messages.error(request, "Invalid email or password.")
                return redirect("login")
        else:
            username = username_or_email  
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")  
        else:
            messages.error(request, "Invalid credentials.")
            return redirect("login")
    return render(request, "login/login.html")

def signupview(request):
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data["password"])  
            user.save()
            messages.success(request, "Signup successful!")
            return redirect("login")  
    else:
        form = UserSignupForm()
    return render(request, "home/signup.html", {"form": form})


def dashboardview(request):
    if not request.user.is_authenticated or not request.user.is_superuser:
        return redirect("login") 

    orders = Order.objects.all().order_by('-order_date')
    status_count = {
        'pending': Order.objects.filter(status=Order.OrderStatus.PENDING).count(),
        'processing': Order.objects.filter(status=Order.OrderStatus.PROCESSING).count(),
        'shipped': Order.objects.filter(status=Order.OrderStatus.SHIPPED).count(),
        'delivered': Order.objects.filter(status=Order.OrderStatus.DELIVERED).count(),
        'cancelled': Order.objects.filter(status=Order.OrderStatus.CANCELLED).count(),
    }

    context = {
        'orders': orders,
        'status_count': status_count,
    }

    return render(request, "home/dashboard.html", context)


def logoutview(request):
    logout(request)
    return redirect("login/login.html")
