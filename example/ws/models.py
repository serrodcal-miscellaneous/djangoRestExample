from django.db import models
import json

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)