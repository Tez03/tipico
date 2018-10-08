from django.shortcuts import render
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

	def vista_conexion(request):
		pass
	return render(request, 'index.html',locals())
