from django.urls import path
from .views import galeria, home , contacto

urlpatterns = [
    path('', home,name='home'),
    path('galeria/', galeria,name='galeria'),
    path('contacto/', contacto,name='contacto'),   
]
