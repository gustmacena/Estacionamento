from django.db import models

class Carro(models.Model):
    placa = models.CharField(max_length=7, unique=True)
    tipo_veiculo = models.CharField(max_length=50)
    proprietario = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.placa

class Vaga(models.Model):
    numero = models.IntegerField(unique=True)
    status = models.CharField(max_length=10, choices=[('livre', 'Livre'), ('ocupada', 'Ocupada')], default='livre')
    carro = models.ForeignKey(Carro, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Vaga {self.numero}"

class Ticket(models.Model):
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_entrada = models.DateTimeField(auto_now_add=True)
    data_saida = models.DateTimeField(null=True, blank=True)
    ticket_id = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.ticket_id