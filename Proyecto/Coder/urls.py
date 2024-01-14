from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index, name='index' ),
    path("Equipo/list", views.equipo_list, name="equipo_list"),
    path("Equipo/form", views.equipo_form, name="equipo_form"),
]
