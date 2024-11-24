from django.shortcuts import render, redirect
from .models import ServiciosEsteticos, TratamientoFacial, TratamientoCorporal
from django.contrib import messages

# Vista principal que lista todos los servicios estéticos
def homeFacial(request):
    ListadoServicios = TratamientoFacial.objects.all()
    ListadoServiciosCorporal = TratamientoCorporal.objects.all()
    messages.success(request, 'Servicio Listado')
    return render(request, "gestionServicios.html", {"ServiciosFacial": ListadoServicios,'ServiciosCorporal': ListadoServiciosCorporal})

# Vista para registrar un nuevo servicio
def RegistrarServicioIdFacial(request):
        IdServicio = request.POST['txtidFAcial']
        registro = ServiciosEsteticos.objects.create(IdServicio=IdServicio)
        messages.success(request, 'Servicio registrado')
        return redirect('/')
def RegistrarFacial(request):
    NombreServicio = request.POST['txtnombreservicioFacial']
    Descripcion = request.POST['txtdescripcionFacial']
    Duracion = request.POST['txtduracionFacial']
    Precio = request.POST['txtprecioFacial']
    TipoTratamiento = request.POST['txtTipoTratamiento']
    TipoPiel = request.POST['txtTipoPiel']
    
    # Crea un nuevo registro en la base de datos
    registro=TratamientoFacial.objects.create( NombreServicio=NombreServicio, Descripcion=Descripcion, Duracion=Duracion, Precio=Precio,TipoTratamiento=TipoTratamiento, tipoPiel=TipoPiel)
    
    messages.success(request, 'Servicio registrado')
    return redirect('/')

# Vista para mostrar los datos de un servicio específico en la página de edición
def EdicionRegistroFacial(request, id):
    registro= TratamientoFacial.objects.get(id=id)
    return render(request, "EdicionRegistro.html", {"registro":registro})

# Vista para editar un servicio existente
def EditarRegistroFacial(request, id):
    NombreServicio = request.POST['nombreServicio']
    Descripcion = request.POST['txtdescripcionFacial']
    Duracion = request.POST['txtduracionFacial']
    Precio = request.POST['txtprecioFacial']
    TipoTratamiento = request.POST['txtTipoTratamiento']
    TipoPiel = request.POST['txtTipoPiel']
    registro= TratamientoFacial.objects.get(id=id)
    registro.NombreServicio = NombreServicio
    registro.Descripcion = Descripcion
    registro.Duracion=Duracion
    registro.Precio = Precio
    registro.TipoTratamiento = TipoTratamiento
    registro.tipoPiel = TipoPiel
    registro.save()
    
    messages.success(request, 'Servicio editado')
    
    return redirect('/')
    
# Vista para redirigir a la misma pagina
def redirigir(request):
    return redirect('gestionServicios.html')

# Vista para eliminar un servicio
def EliminarRegistroFacial(request, id):
    registro=TratamientoFacial.objects.get(id=id)
    registro.delete()
    
    messages.success(request, 'Servicio eliminado')
    
    return redirect('/')

# vistas para tratamiento corporal

# Vista para registrar un nuevo servicio
def RegistrarServicioIdCorporal(request):
        IdServicio = request.POST['txtidCorporal']
        registro = ServiciosEsteticos.objects.create(IdServicio=IdServicio)
        messages.success(request, 'Servicio registrado')
        return redirect('/')
def RegistrarCorporal(request):
    # id = request.POST['txtidCorporal']
    NombreServicio = request.POST['txtnombreservicioCorporal']
    Descripcion = request.POST['txtdescripcionCorporal']
    Duracion = request.POST['txtduracionCorporal']
    Precio = request.POST['txtprecioCorporal']
    ZonaTratada = request.POST['txtZonaTratada']
    TipoProducto = request.POST['txtTipoProducto']
    
    # Crea un nuevo registro en la base de datos
    registro=TratamientoCorporal.objects.create( NombreServicio=NombreServicio, Descripcion=Descripcion, Duracion=Duracion, Precio=Precio,ZonaTratada=ZonaTratada, TipoProducto=TipoProducto )
    messages.success(request, 'Servicio registrado')
    return redirect('/')

# Vista para mostrar los datos de un servicio específico en la página de edición
def EdicionRegistroCorporal(request, id):
    registro= TratamientoCorporal.objects.get(id=id)
    return render(request, "EdicionRegistroCorporal.html", {"registro":registro})

# Vista para editar un servicio existente
def EditarRegistroCorporal(request, id):
    NombreServicio = request.POST['txtnombreservicioCorporal']
    Descripcion = request.POST['txtdescripcionCorporal']
    Duracion = request.POST['txtduracionCorporal']
    Precio = request.POST['txtprecioCorporal']
    ZonaTratada = request.POST['txtZonaTratada']
    TipoProducto = request.POST['txtTipoProducto']
    
    registro= TratamientoCorporal.objects.get(id=id)
    registro.NombreServicio = NombreServicio
    registro.Descripcion = Descripcion
    registro.Duracion=Duracion
    registro.Precio = Precio
    registro.ZonaTratada = ZonaTratada
    registro.TipoProducto = TipoProducto
    registro.save()
    
    messages.success(request, 'Servicio editado')
    
    return redirect('/')
    
# Vista para redirigir a la misma pagina
def redirigir(request):
    return redirect('gestionServicios.html')

# Vista para eliminar un servicio
def EliminarRegistroCorporal(request, id):
    registro=TratamientoCorporal.objects.get(id=id)
    registro.delete()
    
    messages.success(request, 'Servicio eliminado')
    
    return redirect('/')

