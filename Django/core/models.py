from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Modelo para la categoria.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# Modelo para el producto.

class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField()
  
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

# Selector de la clase Modelo
opciones = [
    [0, "Seleccione Region"],
    [1, "region 1"],
    [2, "region 2"],
    [3, "region 3"],
    [4, "region 4"]
]
# Modelo para el contacto
class Contacto(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    region = models.IntegerField(choices=opciones)
    avisos = models.BooleanField()

    def __str__(self):
        return self.name