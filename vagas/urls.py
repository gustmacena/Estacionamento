from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vagas, name='lista_vagas'),
]