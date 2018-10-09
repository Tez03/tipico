from django.shortcuts import render,redirect
from .models import *
from django.urls import reverse_lazy
from django.views.generic.edit import (CreateView)
import requests
import json

# Create your views here.

def vista_conexion(request):
	r = requests.get('https://tipico-saludable-50fb7.firebaseio.com/Deporte.json/')
	r.status_code
	r.headers['content-type']
	r.encoding
	r.text
	x=r.json()
	y=json.dumps(x)
	return render(request, 'prueba.html',locals())

def vista_agregar_comida(request):
	get_comidas = requests.get('https://tipico-saludable-50fb7.firebaseio.com/Comida.json')

	comidas = get_comidas.json()

	lis_comidas=[]
	
	for c in comidas:
		p =  c['nombre'],c['imagen'],c['calorias'],c['carbohidratos'],c['proteinas'],c['descripcion'],c['receta']
		lis_comidas.append(p)

	if request.method == 'POST':			

		nombre = request.POST.get('nombre')
		imagen = request.POST.get('imagen')
		calorias = request.POST.get('calorias')
		carbohidratos = request.POST.get('carbohidratos')
		proteinas = request.POST.getlist('proteinas')
		descripcion = request.POST.get('descripcion')
		receta = request.POST.get('receta')

		metodo_post(nombre,imagen,calorias,carbohidratos,proteinas,descripcion,receta)

		return  redirect ('/agregar_comida/')

	return render(request, 'vista_agregar_comida.html', locals())

def metodo_get():

	peticion = requests.get('https://tipico-saludable-50fb7.firebaseio.com/Comida.json')

	respuesta = peticion.json()
	lista = []
	for i in respuesta:
		cadena = i['url']
		l   = len(cadena)
		id_ = cadena[l-2]
		p   = i['nombre'], id_
		lista.append(p)

	return lista

def metodo_post(nombre,imagen,calorias,carbohidratos,proteinas,descripcion,receta):

	dato = {

        "nombre": nombre,
        "imagen": imagen,
        "calorias": calorias,
        "carbohidratos": carbohidratos,
        "proteinas": proteinas,
        "descripcion": descripcion,
        "receta": receta
    }

	peticion = requests.post('https://tipico-saludable-50fb7.firebaseio.com/Comida.json', data = dato)
	peticion.status_code

	respuesta = peticion.json()
	return respuesta
