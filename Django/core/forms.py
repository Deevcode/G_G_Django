from tkinter import Widget
from django import forms
from .models import Contacto, Producto

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
