from django.urls import path, include
from .views import extra_page, galeria, home , contacto , agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro, politicas , ProductoViewset, CategoriaViewset
from rest_framework import routers

#ROUTERS PARA GENERAR API
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('categoria', CategoriaViewset)


urlpatterns = [
    path('', home,name="home"),
    path('galeria/', galeria,name="galeria"),
    path('contacto/', contacto,name="contacto"),
    path('agregar-producto/', agregar_producto,name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('tienda/', extra_page, name="tienda"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls) ),
    path('politicas/', politicas, name="politicas")
]
