from django.db import models

# Create your models here.

class Usuario(models.Model):

    nombre = models.CharField(max_length=12)
    contraseña = models.CharField(max_length=12)
    email = models.EmailField()

class Personaje(models.Model):

    nombre = models.CharField(max_length=10)
    clase = models.CharField(max_length=10)
    genero = models.CharField(max_length=10)

class Arma(models.Model):

    nombre = models.CharField(max_length=15)
    clase = models.CharField(max_length=15)
    municion = models.CharField(max_length=15)
