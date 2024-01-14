from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    equipo = models.CharField(max_length=100)
    camiseta = models.PositiveIntegerField()
    
    def __str__(self) :
        return f'{self.nombre} {self.apellido}'

class Equipo(models.Model):
    nombre = models.CharField(max_length=100)
    jugadores = models.PositiveIntegerField()
    division = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.nombre}'

class Torneo(models.Model):
    division = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    def __str__(self) :
        return f'{self.categoria} {self.division}'


class JugadorPorEquipo(models.Model):
    nombre = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    apellido = models.ForeignKey(Jugador, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.nombre} {self.apellido}'

class EquipoPorTorneo(models.Model):
    nombre = models.ForeignKey(Equipo, on_delete=models.CASCADE)
    division = models.ForeignKey(Torneo, on_delete=models.CASCADE)

    def __str__(self) :
        return f'{self.nombre} {self.division}'