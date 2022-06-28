from django.urls import path, include
from .views import CategoriaList, extra_page, fundacion, home , contacto , agregar_producto, listar_producto, modificar_producto, eliminar_producto, registro, politicas , ProductoViewset, CategoriaViewset
from rest_framework import routers
from . import views

#ROUTERS PARA GENERAR API
router = routers.DefaultRouter()
router.register('producto', ProductoViewset)
router.register('categoria', CategoriaViewset)


urlpatterns = [
    path('', home,name="home"),
    path('fundacion/', fundacion,name="fundacion"),
    path('contacto/', contacto,name="contacto"),
    path('agregar-producto/', agregar_producto,name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('tienda/', extra_page, name="tienda"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls) ),
    path('politicas/', politicas, name="politicas"),
    path('categoria-list/', CategoriaList.as_view(), name="categoria_list"),
]

login = router.urls

login += path('login', views.login ),