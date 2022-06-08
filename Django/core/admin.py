from django.contrib import admin
from .models import Categoria, Producto , Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria", "imagen"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)