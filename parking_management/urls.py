from django.contrib import admin
from django.urls import path, include
from vagas.views import home  # Importe a view home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vagas/', include('vagas.urls')),
    path('tarifas/', include('tarifas.urls')),
    path('', home, name='home'),  # Rota para a raiz
]