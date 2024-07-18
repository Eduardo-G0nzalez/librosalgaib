from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib.messages import get_messages
from .models import Product
from .forms import CustomUserCreationForm, CustomAuthenticationForm, ContactoForm

def product_list(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(
            Q(nombre__icontains=query) |
            Q(autor__icontains=query)
        ).order_by('-fecha_ingreso')
    else:
        products = Product.objects.all().order_by('-fecha_ingreso')
    return render(request, 'product_list.html', {'products': products})

def raw_product_list(request):
    query = request.GET.get('q')
    with connection.cursor() as cursor:
        if query:
            cursor.execute("SELECT * FROM store_product WHERE nombre LIKE %s OR autor LIKE %s", ['%' + query + '%', '%' + query + '%'])
        else:
            cursor.execute("SELECT * FROM store_product")
        products = cursor.fetchall()
    return render(request, 'raw_product_list.html', {'products': products})

def index(request):
    products = Product.objects.order_by('-fecha_ingreso')[:12]
    return render(request, 'index.html', {'products': products})

def libro_detalle(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'libro_detalle.html', {'product': product})

def registro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('index')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('login')

def contacto_view(request):
    storage = get_messages(request)
    list(storage)

    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Gracias por contactarnos! Nos pondremos en contacto contigo pronto.')
            return redirect('contacto')
    else:
        form = ContactoForm()
    return render(request, 'contacto.html', {'form': form})