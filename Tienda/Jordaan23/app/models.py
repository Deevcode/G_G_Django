from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# MODELO PARA CATEGORIA DEL PRODUCTO.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre

# MODELO DE PRODUCTO.(TIENE HERENCIA DE CLASE PRODUCTO)
class Producto(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    fecha_publicacion = models.DateField(auto_now_add=True)
  
    imagen = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre

# SELECTOR DEL MODELO DE CONTACTO
opciones = [
    [0, "Seleccione Consulta"],
    [1, "Envios a regiones"],
    [2, "Compras mayoristas"],
    [3, "Banquetera"],
    [4, "Eventos masivos"]
]
# MODELO DE CONTACTO
class Contacto(models.Model):
    name = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField()
    consulta = models.IntegerField(choices=opciones)
    terminos = models.BooleanField()
    texto = models.TextField()

    def __str__(self):
        return self.name