from django.contrib import admin

from . import models

admin.site.register(models.Jugador)
admin.site.register(models.Equipo)
admin.site.register(models.Torneo)
admin.site.register(models.JugadorPorEquipo)
