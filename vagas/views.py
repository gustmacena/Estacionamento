from django.shortcuts import render
from .models import Vaga

def home(request):
    return render(request, 'vagas/home.html', {'titulo': 'Gerenciamento de Estacionamento'})

def lista_vagas(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas/lista_vagas.html', {'vagas': vagas})