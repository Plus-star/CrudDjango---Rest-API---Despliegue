from rest_framework import serializers
from .models import ServiciosEsteticos
from .models import TratamientoFacial
from .models import TratamientoCorporal

class ServiciosEsteticosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiciosEsteticos
        fields = ('id', 'NombreServicio', 'Descripcion', 'Duracion', 'Precio')
        
class TratamientoFacialSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoFacial
        fields = ('id', 'NombreServicio', 'Descripcion', 'Duracion', 'Precio', 'TipoTratamiento', 'tipoPiel')

class TratamientoCorporalSerializer(serializers.ModelSerializer):
    class Meta:
        model = TratamientoCorporal
        fields = ('id', 'NombreServicio', 'Descripcion', 'Duracion', 'Precio', 'ZonaTratada', 'TipoProducto')
