from django.contrib import admin
from .models import Marca, Producto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "marca", "imagen"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    

admin.site.register(Marca)
admin.site.register(Producto, ProductoAdmin)