from django.db import models 

# Modelo que representa un servicio estético
class ServiciosEsteticos(models.Model):
    
    NombreServicio=models.CharField(max_length=100, default = '1')
    Descripcion=models.CharField(max_length=100,default = '1')
    Duracion=models.CharField(max_length=50,default = '1')
    Precio=models.CharField(max_length=50, default = '10')
    
    # Representación del objeto como cadena (para que se muestre en la interfaz de Django)
    def __str__(self):
        texto= "{0} ({1})"
        return texto.format(self.IdServicio, self.NombreServicio, self.Descripcion, self.Duracion, self.Precio)

class TratamientoFacial(ServiciosEsteticos):
    TipoTratamiento=models.CharField(max_length=100)
    tipoPiel=models.CharField(max_length=100)

class TratamientoCorporal(ServiciosEsteticos):
    ZonaTratada=models.CharField(max_length=100)
    TipoProducto=models.CharField(max_length=100)

