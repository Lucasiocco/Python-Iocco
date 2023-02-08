from django.shortcuts import render
from django.http import HttpResponse
from AppIocco.models import Personaje

# Create your views here.

def inicio(request):

    return HttpResponse("Bienvenido/a.")

def personajes(request):

    personaje1 = Personaje(nombre="Lifeline", clase="Soporte", genero="Femenino")
    personaje1.save()
    personaje2 = Personaje(nombre="Bangalore", clase="Asesina", genero="Femenino")
    personaje2.save()

    return HttpResponse("Personajes")