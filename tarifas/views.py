from django.shortcuts import render
from .models import Tarifa

def lista_tarifas(request):
    tarifas = Tarifa.objects.all()
    return render(request, 'tarifas/lista_tarifas.html', {'tarifas': tarifas})