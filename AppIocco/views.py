from django.shortcuts import render
from django.http import HttpResponse
from AppIocco.models import *
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def inicio(request):

    return render(request, "AppIocco/index.html")

def registro(request):

    if request.method == "POST":

        miFormulario = UserCreationForm(request.POST)

        if miFormulario.is_valid():

            miFormulario.save()

            return render(request, "AppIocco/index.html")
    
    else:

        miFormulario = UserCreationForm()

    return render(request, "AppIocco/autentificacion/resgistro.html", {"miFormulario":miFormulario})

def usuario(request):

    return render(request, "AppIocco/usuario.html")




class ArmaLista(ListView):
    model = Arma

class ArmaCrear(CreateView):
    model = Arma
    fields = ["nombre", "clase", "municion"]
    success_url = "/AppIocco/arma_form.html"

class ArmaBorrar(DeleteView):
    model = Arma
    success_url = "/AppIocco/arma_confirm_delete.html"

class ArmaEditar(UpdateView):
    model = Personaje
    fields = ["nombre", "clase", "municion"]
    success_url = "/AppIocco/arma_list.html"
    
class PersonajeLista(ListView):
    model = Personaje

class PersonajeCrear(CreateView):
    model = Personaje
    fields = ["nombre", "clase", "genero"]
    success_url = "/AppIocco/personaje_form.html"

class PersonajeBorrar(DeleteView):
    model = Personaje
    success_url = "/AppIocco/personaje_confirm_delete.html"

class PersonajeEditar(UpdateView):
    model = Personaje
    fields = ["nombre", "clase", "genero"]
    success_url = "/AppIocco/personaje_list.html"
