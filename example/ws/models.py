from django.db import models

class Departamento(models.Model):
    id = models.IntegerField(null=False)
    nombre = models.CharField(max_length=100)

class Empleado(models.Model):
    id = models.IntegerField(null=False)
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento)