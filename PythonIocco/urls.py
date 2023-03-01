from django.contrib import admin
from django.urls import path
from AppIocco.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("inicio/", inicio, name="Inicio"),
    path("usuario/", usuario, name="Usuario"),
    path("registro/", registro, name="Sign Up"),

#Crud de Armas
    path("arma_list/", ArmaLista.as_view(), name="Armas"),
    path("arma_form/", ArmaCrear.as_view(), name="Crear Arma"),
    path("arma_confirm_delete/<int:pk>", ArmaBorrar.as_view(), name="Borrar Arma"),
    path("arma_list/<int:pk>", ArmaEditar.as_view(), name="Editar Arma"),

#Crud de Personajes
    path("personaje_list/", PersonajeLista.as_view(), name="Personajes"),
    path("personaje_form/", PersonajeCrear.as_view(), name="Crear Personaje"),
    path("personaje_confirm_delete/<int:pk>", PersonajeBorrar.as_view(), name="Borrar Personaje"),
    path("personaje_list/<int:pk>", PersonajeEditar.as_view(), name="Editar Personaje"),

]