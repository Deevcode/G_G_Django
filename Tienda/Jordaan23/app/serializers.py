from .models import Categoria, Producto
from rest_framework import serializers
from django.forms import ValidationError

class CategoriaSerializar(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

# SERIALIZER PARA PRODUCTOS JSON
class ProductoSerializer(serializers.ModelSerializer):

    #--------------------------------------------  CATEGORIA   --------------------------------------------
    #INSERTAR EL NOMBRE DE LA MARCA EN EL JSON (SERIALIERS)
    nombre_categoria = serializers.CharField(read_only=True, source="categoria.nombre")
    # INSERTA DETALLES DE LA CATEGORIA
    categoria = CategoriaSerializar(read_only=True)
    # INSERTA ID DE LA CATEGORIA
    categoria_id = serializers.PrimaryKeyRelatedField(queryset=Categoria.objects.all(), source="categoria")
    #-------------------------------------------------------------------------------------------------------

    #----------------------------------------------  NOMBRE   ----------------------------------------------
    nombre = serializers.CharField(required=True)

    # VALIDAR SI EL PRODUCTO YA EXISTE EN LA API
    def validate_nombre(self, value):
        existe = Producto.objects.filter(nombre__iexact=value).exists()
        if existe:
            raise serializers.ValidationError("Este nombre ya existe")
        return value    
    #-------------------------------------------------------------------------------------------------------

    #----------------------------------------------  ID   ----------------------------------------------
    #id = serializers.CharField(required=True)

    # VALIDAR SI EL ID YA EXISTE EN LA API
    #def validate_id(self, value):
    #    existe = Producto.objects.filter(id=id).exists()
    #    if existe:
    #        raise serializers.ValidationError("Este ID ya existe")
    #    return value    
    #-------------------------------------------------------------------------------------------------------

    class Meta:
        model = Producto
        fields = '__all__'