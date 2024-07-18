from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import contacto_view

urlpatterns = [
    path('', views.index, name='index'), 
    path('products/', views.product_list, name='product_list'),
    path('raw/', views.raw_product_list, name='raw_product_list'),
    path('bookdetail/<int:product_id>/', views.libro_detalle, name='libro_detalle'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', contacto_view, name='contacto'),
]