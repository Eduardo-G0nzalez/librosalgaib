from django.db import models

class Product(models.Model):
    nombre = models.TextField()
    autor = models.TextField()
    editorial = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=6, decimal_places=0)
    stock = models.IntegerField()
    paginas = models.IntegerField()
    descripcion = models.TextField()
    fecha_ingreso = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.nombre
    
class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
