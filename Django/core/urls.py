from django.urls import path
<<<<<<< HEAD
from .views import fundacion_page, galeria, home , contacto , agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro
=======
from .views import fundacion_page, galeria, home , contacto , agregar_producto, listar_producto, modificar_producto, eliminar_producto
>>>>>>> ramaD

urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
    path('agregar-producto/', agregar_producto,name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('fundacion/', fundacion_page, name="fundacion"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
<<<<<<< HEAD
    path('registro/', registro, name="registro"),
=======
>>>>>>> ramaD
]
