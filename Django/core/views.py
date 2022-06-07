from email import message
import re
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
<<<<<<< HEAD
from .forms import  ContactoForm, CustomUserCreationForm , ProductoForm , UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
=======
from .forms import  ContactoForm , ProductoForm
from django.contrib import messages
>>>>>>> ramaD

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
            messages.success(request, "Producto registrado")
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

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=objeto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_producto")
        data['form'] = formulario

    return render(request, 'core/productos/modificar.html', data)

# VISTA DE ELIMINAR HTML #    
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
<<<<<<< HEAD
    return redirect(to="listar_producto")

# VISTA DE ELIMINAR HTML #
def  registro(request):
    data = {
        'form' : UserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            #REDIRIGIR AL HOME
            return redirect(to="home")
        data['form'] = formulario    

    return render(request, 'registration/registro.html', data)
=======
    return redirect(to="listar_producto")
>>>>>>> ramaD
