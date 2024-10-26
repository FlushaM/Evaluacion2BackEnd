from django.db import models
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, RegexValidator


class Equipo(models.Model):
    nombre = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z ]*$',
                message='Nombre invalido, solo letras.'
            )
        ]
    )
    ciudad = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z ]*$',
                message='Nombre invalido, solo letras.'
            )
        ]
    )
    campeonatos = models.IntegerField(
        validators=[
            MinValueValidator(0, message='El número de campeonatos no puede ser negativo')
        ]
    )
    conferencia = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z ]*$',
                message='Nombre invalido, solo letras.'
            )
        ]
    )
    estadio = models.CharField(max_length=100)
    colores = models.CharField(
        max_length=30,
        validators=[
            RegexValidator(
                regex='^[a-zA-Z ]+$',
                message='Color invalido solo letras',
                code='invalid_nombre'
            )
        ])
    liga = models.CharField(max_length=100)