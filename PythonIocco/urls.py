from django.contrib import admin
from django.urls import path
from AppIocco.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", inicio, name="Inicio"),
    path("ver_personajes/", ver_personajes, name="Personajes"),
    path("ver_armas/", ver_armas, name="Armas"),
    path("crear_usuario", crear_usuario, name="Usuario"),
]
 