from django.shortcuts import render
from django.http import HttpResponse
from AppIocco.models import Personaje, Arma, Usuario

# Create your views here.

def inicio(request):

    return render(request, "AppIocco/index.html")

def ver_personajes(request):

    listaPersonajes = Personaje.objects.all

    return render(request, "AppIocco/personajes.html", {"listaPersonajes":listaPersonajes})

def ver_armas(request):

    listaArmas = Arma.objects.all

    return render(request, "AppIocco/armas.html", {"listaArmas":listaArmas})

def ver_usuario(request):

    return render(request, "AppIocco/usuario.html")

def crear_usuario(request):

    if request.method == "POST":

        usuario = Usuario (nombre = request.POST["nombre"], contraseña = request.POST["contraseña"], email = request.POST["email"])

        usuario.save()

    return render(request, "AppIocco/usuario.html")

    
