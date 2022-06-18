from email import message
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Categoria
from .forms import  ContactoForm, CustomUserCreationForm , ProductoForm , UserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
from rest_framework import viewsets
from .serializers import ProductoSerializer, CategoriaSerializar

# Create your views here.

#----------------------------------------------  SERIALIZER (JSON)   ----------------------------------------------
#SERIALIZADOR PARA CONVERTIR LOS PRODUCTOS A JSON [ 127.0.0.1:8000/api/categoria/1/  (id)]
class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializar

#SERIALIZADOR PARA CONVERTIR LOS PRODUCTOS A JSON [ 127.0.0.1:8000/api/producto/1/  (id)]
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    #BUSCAR PRODUCTO POR NOMBRE DESDE EL SERIALIZER EN JSON  [ 127.0.0.1:8000/api/producto/?nombre=pala  (nombre)]
    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre) # CONTAINS ES LO MISMO QUE EL 'LIKE' EN BASE DE DATOS
        return productos    
#-------------------------------------------------------------------------------------------------------

#------------------------------------------|
# VERIFICAR LOGIN PARA ACCEDER A LA PAGINA |
#@login_required                           |
#------------------------------------------|

# VISTA DE HOME HTML #
def home (request):
    productos = Producto.objects.all()
    data = {
        'entity' : productos
    }
    return render(request, 'app/home.html', data)

# VISTA DE GALERIA HTML #
def galeria(request):
    return render(request, 'app/galeria.html') 

# VISTA DE FUNDACION # 
def extra_page(request):
    return render(request, 'app/tienda.html')  

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
    return render(request, 'app/contacto.html', data)

# PERMISO PARA AGREGAR PRODUCTO
@permission_required('app.add_producto')
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


    return render(request, 'app/productos/agregar.html', data)

# PERMISO PARA LISTAR PRODUCTO
@permission_required('app.view_producto')
# VISTA DE LISTAR PRODUCTO HTML #
def listar_producto(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404


    data = {
        'entity' : productos,
        'paginator' : paginator
    }

    return render(request, 'app/productos/listar.html', data)

# PERMISO PARA MODIFICAR PRODUCTO
@permission_required('app.change_producto')
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

    return render(request, 'app/productos/modificar.html', data)

# PERMISO PARA ELIMINAR PRODUCTO
@permission_required('app.delete_producto')
# VISTA DE ELIMINAR HTML #    
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_producto")

#VISTA DE POLITICAS PARA FACEBOOK
def politicas(request):
    return render(request, 'app/politicas.html')

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