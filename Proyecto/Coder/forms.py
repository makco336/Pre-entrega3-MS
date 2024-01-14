from django import forms
from . import models

class equipoform(forms.ModelForm):
    class Meta:
        model = models.Equipo
        fields = "__all__"

class jugadorform(forms.ModelForm):
    class Meta:
        model = models.Jugador
        fields = "__all__"

class torneoform(forms.ModelForm):
    class Meta:
        model = models.Torneo
        fields = "__all__"

class equipoportorneoform(forms.ModelForm):
    class Meta:
        model = models.EquipoPorTorneo
        fields = "__all__"

class jugadorporequipoform(forms.ModelForm):
    class Meta:
        model = models.JugadorPorEquipo
        fields = "__all__"