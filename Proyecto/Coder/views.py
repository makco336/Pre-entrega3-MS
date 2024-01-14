from django.shortcuts import render, redirect
from . import models
from . import forms

def index(request):
    return  render(request, "Coder/index.html")

def equipo_list(request):
    consulta =  models.Equipo.objects.all()
    contexto = {"Equipos": consulta}
    return render(request, "Coder/equipo_list.html", contexto)

def equipo_form(request):
    if request.method =="POST":
        form = forms.equipoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("equipo_list")
    else:
        form = forms.equipoform()
    return render(request, "Coder/equipo_form.html", {"form": form})

def jugador_list(request):
    consulta =  models.Jugador.objects.all()
    contexto = {"Jugador": consulta}
    return render(request, "Coder/jugador_list.html", contexto)

def jugador_form(request):
    if request.method =="POST":
        form = forms.jugadorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("jugador_list")
    else:
        form = forms.jugadorform()
    return render(request, "Coder/jugador_form.html", {"form": form})

def torneo_list(request):
    consulta =  models.Torneo.objects.all()
    contexto = {"Torneo": consulta}
    return render(request, "Coder/torneo_list.html", contexto)

def torneo_form(request):
    if request.method =="POST":
        form = forms.torneoform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("torneo_list")
    else:
        form = forms.torneoform()
    return render(request, "Coder/torneo_form.html", {"form": form})
