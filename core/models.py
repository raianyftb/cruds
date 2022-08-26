from django.db import models

class Cafe(models.Model): 
    marca = models.CharField('Marca', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    quantidade = models.IntegerField('Quantidade')

