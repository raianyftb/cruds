from distutils.archive_util import make_zipfile
from django.db import models

class Produtos(models.Model): 
    nome = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    quantidade = models.IntegerField('Quantidade')
    descricao = models.CharField('Descrição', max_length=200)
     

