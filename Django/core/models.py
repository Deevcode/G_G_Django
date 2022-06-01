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

opciones = [
    [0, "Seleccione Region"],
    [1, "region 1"],
    [2, "region 2"],
    [3, "region 3"],
    [4, "region 4"]
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    region = models.TextField(choices=opciones)
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre