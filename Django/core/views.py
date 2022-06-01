from operator import imod
from unicodedata import name
from django.shortcuts import render
from .models import Producto
from .forms import Contacto, ContactoForm

# Create your views here.

# VISTA DE HOME HTML #
def home (request):
    productos = Producto.objects.all()
    data = {
        'productos' : productos
    }
    return render(request, 'core/home.html', data)

# VISTA DE GALERIA HTML #
def galeria(request):
    return render(request, 'core/galeria.html') 

# VISTA DE CONTACTO HTML #

def contacto(request):
    data = {
        'form' : ContactoForm()
    }
    return render(request, 'core/contacto.html', data)