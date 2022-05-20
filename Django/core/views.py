from unicodedata import name
from django.shortcuts import render

# Create your views here.
def home (request):
    return render(request, 'core/home.html')

def galeria(request):
    return render(request, 'core/galeria.html')    