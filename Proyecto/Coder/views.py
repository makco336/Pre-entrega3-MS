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

