from django.db import models

class Tarifa(models.Model):
    tipo_veiculo = models.CharField(max_length=50)
    valor_hora = models.DecimalField(max_digits=5, decimal_places=2)
    dia_semana = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.tipo_veiculo} - {self.valor_hora}/h"