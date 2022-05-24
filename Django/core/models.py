from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo para el Vehiculo

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField()
  
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre