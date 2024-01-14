from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index, name='index' ),
    path("Equipo/list", views.equipo_list, name="equipo_list"),
    path("Equipo/form", views.equipo_form, name="equipo_form"),
    path("Jugador/list", views.jugador_list, name="jugador_list"),
    path("Jugador/form", views.jugador_form, name="jugador_form"),
    path("Torneo/list", views.torneo_list, name="torneo_list"),
    path("Torneo/form", views.torneo_form, name="torneo_form"),
    path("EquipoPorTorneo/list", views.equipoportorneo_list, name="equipoportorneo_list"),
    path("EquipoPorTorneo/form", views.equipoportorneo_form, name="equipoportorneo_form"),
    path("JugadorPorEquipo/list", views.jugadorporequipo_list, name="jugadorporequipo_list"),
    path("JugadorPorEquipo/form", views.jugadorporequipo_form, name="jugadorporequipo_form"),
]
