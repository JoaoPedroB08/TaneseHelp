from django.db import models
from django.contrib.auth.models import User

class Caixa(models.Model):
    dono = models.ForeignKey(User, on_delete=models.CASCADE)
    identificacao = models.CharField(max_length=100)

    def __str__(self):
        return self.identificacao

class Ferramenta(models.Model):
    caixa = models.ForeignKey(Caixa, on_delete=models.PROTECT)
    nome = models.CharField(max_length=100)
    descricao = models.CharField(max_length=255)

    def __str__(self):
        return self.nome