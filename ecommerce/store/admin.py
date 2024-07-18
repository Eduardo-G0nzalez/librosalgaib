from django.contrib import admin
from .models import Product, Contacto

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'editorial', 'precio', 'stock', 'paginas', 'descripcion', 'fecha_ingreso', 'imagen')
    search_fields = ('nombre', 'autor')
    list_filter = ('fecha_ingreso',)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'email', 'fecha')
    search_fields = ('nombre', 'email')
    list_filter = ('fecha',)