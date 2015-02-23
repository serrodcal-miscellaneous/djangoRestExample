from django.shortcuts import render
from django.core import serializers
from ws.models import Empleado, Departamento
from django.http import HttpResponse
import json

def empleados(request):
    empleados = Empleado.objects.all()
    # return conversion a json de la lista de empleados