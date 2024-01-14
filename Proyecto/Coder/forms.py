from django import forms
from . import models

class equipoform(forms.ModelForm):
    class Meta:
        model = models.Equipo
        fields = "__all__"