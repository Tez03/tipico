from django.urls import path
from .views import * 

urlpatterns = [
    path('conexionfirebase/',vista_conexion,name='conexion'),
    path('index/',index,name='index'),

]
