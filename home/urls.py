from django.urls import path
from django.views.generic import TemplateView
from .views import * 

urlpatterns = [
    path('conexionfirebase/',vista_conexion,name='conexion'),
    path('agregar_comida/',vista_agregar_comida,name='agregar_comida'),
]
