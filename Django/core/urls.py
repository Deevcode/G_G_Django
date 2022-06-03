from django.urls import path
from .views import galeria, home , contacto , agregar_producto

urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
    path('agregar-producto/', agregar_producto,name="agregar_producto"),   
]
