# Generated by Django 5.0.1 on 2024-01-13 15:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('jugadores', models.PositiveIntegerField()),
                ('division', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('equipo', models.CharField(max_length=100)),
                ('camiseta', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Torneo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(max_length=100)),
                ('categoria', models.CharField(max_length=100)),
                ('ult_posicion', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='JugadorPorEquipo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coder.equipo')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coder.jugador')),
            ],
        ),
    ]