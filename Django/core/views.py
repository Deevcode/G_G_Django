from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .forms import  ContactoForm , ProductoForm

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

# VISTA DE FUNDACION # 
def fundacion_page(request):
    return render(request, 'core/fundacion.html')  

# VISTA DE CONTACTO HTML #
def contacto(request):
    data = {
        'form' : ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"]  = formulario  
    return render(request, 'core/contacto.html', data)

# VISTA DE AGREGAR PRODUCTO HTML #
def agregar_producto(request):
    data = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Guardado Correctamente"
        else:
            data['form'] = formulario    


    return render(request, 'core/productos/agregar.html', data)

# VISTA DE LISTAR PRODUCTO HTML #
def listar_producto(request):
    productos = Producto.objects.all()

    data = {
        'productos' : productos
    }

    return render(request, 'core/productos/listar.html', data)

# VISTA DE MODIFICAR HTML #
def modificar_producto(request, id):
    objeto = get_object_or_404(Producto, id=id)
    data = {
        'form': ProductoForm(instance=objeto)
    }
    return render(request, 'core/productos/modificar.html', data)
