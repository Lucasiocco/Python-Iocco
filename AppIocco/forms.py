from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class UsuarioFormulario(forms.form):
    nombre = forms.CharField(max_length=15)
    contraseña = forms.CharField(max_length=15)

class ArmaFormulario(forms.form):
    nombre = forms.CharField(max_length=15)
    clase = forms.CharField(max_length=15)
    municion = forms.CharField(max_length=15)

class PersonajeFormulario(forms.form):
    nombre = forms.CharField(max_length=15)
    clase = forms.CharField(max_length=15)
    genero = forms.CharField(max_length=15)

class RegistroFormulario(UserCreationForm):
    nombre = forms.CharField(max_length=15)
    contraseña = forms.CharField(max_length=15)
    email = forms.EmailField(max_length=40)
