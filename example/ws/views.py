from django.shortcuts import render
from django.core import serializers

def empleados(request):
    empleados = Empleado.objects.all()
    data = serializers.serialize("json", empleados)
    return HttpResponse(data, content_type='application/json')
