from collections import UserString
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#FORMULARIO PARA CONTACTO
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

#FORMULARIO PARA AGREGAR PRODUCTOS
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            "fecha_publicacion": forms.SelectDateWidget()
        }

#FORMULARIO PARA REGISTRO
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password1', 'password2']        
