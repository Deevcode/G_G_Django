from email import message
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect


from .models import Producto, Categoria
from .forms import  ContactoForm, CustomUserCreationForm , ProductoForm , UserCreationForm

from .serializers import ProductoSerializer, CategoriaSerializar

from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect

#IMPORTACIONES DE DJANGO CONTRIB
from django.views.generic.edit import FormView
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import AuthenticationForm

#IMPORTACIONES DE REST FRAMEWORK
from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework import viewsets



# Create your views here.

#----------------------------------------------  SERIALIZER (JSON)   ----------------------------------------------


#-------------------------------------  ACCESO A LOGIN DE LAS APIS (JSON)   ----------------------------------------
class Login(FormView):
    template_name = "access.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('api:categoria_list')

    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(Login,self).dispatch(request,*args,*kwargs)

    def form_valid(self,form):
        user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
        token,_ = Token.objects.get_or_create(user = user)
        if token:
            login(self.request, form.get_user())
            return super(Login,self).form_valid(form)

class Logout(APIView):
    def get(self,request, format = None):
        request.user.auth_token.delete()
        logout(request)
        return Response(status = status.HTTP_200_OK)
#------------------------------------------------------------------------------------------------------------------



#----------------------------------------------  SERIALIZER (JSON)   ----------------------------------------------
#SERIALIZADOR PARA CONVERTIR LOS PRODUCTOS A JSON [ 127.0.0.1:8000/api/categoria/1/  (id)]
class CategoriaViewset(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializar
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

class CategoriaList(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializar
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

#SERIALIZADOR PARA CONVERTIR LOS PRODUCTOS A JSON [ 127.0.0.1:8000/api/producto/1/  (id)]
class ProductoViewset(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)
    
    #BUSCAR PRODUCTO POR NOMBRE DESDE EL SERIALIZER EN JSON  [ 127.0.0.1:8000/api/producto/?nombre=pala  (nombre)]
    def get_queryset(self):
        productos = Producto.objects.all()
        nombre = self.request.GET.get('nombre')

        if nombre:
            productos = productos.filter(nombre__contains=nombre) # CONTAINS ES LO MISMO QUE EL 'LIKE' EN BASE DE DATOS
        return productos    
#-------------------------------------------------------------------------------------------------------------------

#------------------------------------------|
# VERIFICAR LOGIN PARA ACCEDER A LA PAGINA |
#@login_required                           |
#------------------------------------------|
#-------------------------------------------  VISTAS  ---------------------------------------------------------------
# VISTA DE HOME HTML #
def home (request):
    return render(request, 'app/home.html')

# VISTA DE GALERIA HTML #
def galeria(request):
    return render(request, 'app/galeria.html') 

@login_required
# VISTA DE TIENDA # 
def extra_page(request):
    productos = Producto.objects.all()
    data = {
        'entity' : productos
    }
    return render(request, 'app/tienda.html', data)  

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
#-------------------------------------------------------------------------------------------------------------------

#--------------------------------------------- VISTAS CON PERMISOS -----------------------------------------------
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

#VISTA DE POLITICAS
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
#-------------------------------------------------------------------------------------------------------------------    