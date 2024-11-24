from django.urls import path, include
from . import views
from rest_framework import routers
from .api import ServiciosEsteticosViewSet, TratamientoFacialViewSet, TratamientoCorporalViewSet

router = routers.DefaultRouter()
router.register(r'serviciosesteticos', ServiciosEsteticosViewSet)
router.register(r'tratamientosfaciales', TratamientoFacialViewSet)
router.register(r'tratamientoscorporales', TratamientoCorporalViewSet)

urlpatterns = [
    path('api/CrudServiciosEsteticos/', include(router.urls)), 
    path('api/CrudTratamientoFacial/', include(router.urls)),  
    path('api/CrudTratamientoCorporal/', include(router.urls)), 

    path('', views.homeFacial, name='homeFacial'),
    path('EliminarRegistroFacial/<int:id>/', views.EliminarRegistroFacial, name='EliminarRegistroFacial'),
    path('EdicionRegistroFacial/<int:id>/', views.EdicionRegistroFacial, name='EdicionRegistroFacial'),
    path('redirigir', views.redirigir, name='redirigir'),
    path('EditarRegistroCorporal/', views.EditarRegistroCorporal, name='EditarRegistroCorporal'),
    path('RegistrarCorporal/', views.RegistrarCorporal, name='RegistrarCorporal'),
    path('EliminarRegistroCorporal/<int:id>/', views.EliminarRegistroCorporal, name='EliminarRegistroCorporal'),
    path('EdicionRegistroCorporal/<int:id>/', views.EdicionRegistroCorporal, name='EdicionRegistroCorporal'),
    path('EditarRegistroCorporal/<int:id>', views.EditarRegistroCorporal, name='EditarRegistroCorporal'),
    path('RegistrarCorporal/', views.RegistrarCorporal, name='RegistrarCorporal'),
    path('RegistrarServicioIdFacial/', views.RegistrarServicioIdFacial, name='RegistrarServicioIdFacial'),
    path('RegistrarServicioIdCorporal/', views.RegistrarServicioIdCorporal, name='RegistrarServicioIdCorporal'),
    path('RegistrarFacial/', views.RegistrarFacial, name='RegistrarFacial'),
    path('EditarRegistroFacial/<int:id>', views.EditarRegistroFacial, name='EditarRegistroFacial'),
]
