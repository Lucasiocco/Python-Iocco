from django.shortcuts import render
from django.http import HttpResponse
from AppIocco.models import Personaje, Arma, Usuario

# Create your views here.

def inicio(request):

    return render(request, "AppIocco/index.html")

def ver_personajes(request):

    personaje1 = Personaje(nombre="Lifeline", clase="Soporte", genero="Femenino")
    personaje1.save()
    personaje2 = Personaje(nombre="Bangalore", clase="Asesina", genero="Femenino")
    personaje2.save()
    personaje3 = Personaje(nombre="Bloodhound", clase="Cazador", genero="Masculino")
    personaje3.save()

    return render(request, "AppIocco/personajes.html")

def ver_armas(request):

    arma1 = Arma(nombre="R99", clase="Subfusil", municion="Liviana")
    arma1.save()
    arma2 = Arma(nombre="Peacekeeper", clase="Escopeta", municion="Pesada")
    arma2.save()
    arma3 = Arma(nombre="Flatline", clase="Fusil", municion="Media")
    arma3.save()

    return render(request, "AppIocco/armas.html")

def crear_usuario(request):

    if request.method == "POST":

        usuario = Usuario (nombre = request.POST["nombre"], contraseña = request.POST["contraseña"], email = request.POST["email"])

        usuario.save()

    return render(request, "AppIocco/usuario.html")

     
