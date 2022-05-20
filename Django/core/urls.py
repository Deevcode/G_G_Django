from django.urls import path
from .views import galeria, home 

urlpatterns = [
    path('', home,name='home'),
    path('galeria/', galeria,name='galeria'),   
]
