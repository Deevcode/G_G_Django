from unicodedata import name
from django.shortcuts import render

# Create your views here.

# VISTA DE HOME HTML #
def home (request):
    return render(request, 'core/home.html')

# VISTA DE GALERIA HTML #
def galeria(request):
    return render(request, 'core/galeria.html') 

# VISTA DE CONTACTO HTML #

def contacto(request):
    return render(request, 'core/contacto.html')