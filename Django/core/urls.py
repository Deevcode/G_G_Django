from django.urls import path
from .views import fundacion_page, galeria, home , contacto , agregar_producto, listar_producto

urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
    path('agregar-producto/', agregar_producto,name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('fundacion/', fundacion_page, name="fundacion"),
]
