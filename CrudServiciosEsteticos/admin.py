from django.contrib import admin
from .models import ServiciosEsteticos, TratamientoFacial, TratamientoCorporal

admin.site.register(ServiciosEsteticos)
admin.site.register(TratamientoCorporal)
admin.site.register(TratamientoFacial)