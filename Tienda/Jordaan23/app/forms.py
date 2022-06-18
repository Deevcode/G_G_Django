from collections import UserString
from email.mime import image
from xml.dom import ValidationErr
from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .validators import MaxSizeFileValidator
from django.forms import ValidationError

#FORMULARIO PARA CONTACTO
class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'

#FORMULARIO PARA AGREGAR PRODUCTOS
class ProductoForm(forms.ModelForm):

    # VALIDACIONES INTEGRADAS
    id = forms.IntegerField(min_value=1)
    nombre = forms.CharField(min_length=3, max_length=50)
    #IMPORTA VALIDADOR DE TAMAÑO DE LA IMAGEN
    imagen = forms.ImageField(required=False, validators=[MaxSizeFileValidator(max_file_size=2)])
    precio = forms.IntegerField(min_value=1, max_value=1500000)

    # VALIDACION SI EL ID YA EXISTE
    def clean_id(self):
        id = self.cleaned_data["id"]
        existe = Producto.objects.filter(id=id).exists()
        if existe:
            raise ValidationError("Este ID ya existe, escoje otro")
        return id    


    # VALIDACIONES SI EL NOMBRE DEL PRODUCTO YA EXISTE
    def clean_nombre(self):
        nombre = self.cleaned_data["nombre"]
        #METODO DE MODIFICACION DE COINCIDENCIAS EN LA VARIABLE NOMBRE
        existe = Producto.objects.filter(nombre__iexact=nombre).exists()
        if existe:
            raise ValidationError("Este nombre ya existe, iserte otro nombre")
        return nombre    

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
        fields = ['username',"first_name", "last_name", "email", "password1", "password2"]        
