from django.db import models
from django.core.validators import *

# Create your models here.

class Formacao(models.Model):
    data_inicio = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(2030)])
    data_fim = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(2000), MaxValueValidator(2030)])
    escola = models.CharField(max_length=50)
    curso = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500, default='')

    def __str__(self):
        return "[" + str(self.data_inicio) + "-" + str(self.data_fim) + "]" + "  " + self.escola + " - " + self.curso

class Participacao(models.Model):
    data_inicio = models.DateField()
    data_fim = models.DateField(null=True, blank=True)
    titulo = models.CharField(max_length=50)
    localizacao = models.CharField(max_length=50)

    def __str__(self):
        return "[" + str(self.data_inicio) + "/" + str(self.data_fim) + "]" + "  " + self.titulo

    def clean(self):
        if self.data_fim and self.data_fim < self.data_inicio:
            raise ValidationError("A data de fim deve ser posterior à data de início.")


class Interesse(models.Model):
    titulo = models.CharField(max_length=50)
    descricao = models.TextField(max_length=500, default='')

    def __str__(self):
        return self.titulo