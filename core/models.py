from distutils.archive_util import make_zipfile
from django.db import models

class Produtos(models.Model): 
    nome = models.CharField('Nome', max_length=100)
    tipo = models.CharField('Tipo', max_length=100)
    marca = models.CharField('Marca', max_length=100)
    quantidade = models.IntegerField('Quantidade')
    descricao = models.CharField('Descrição', max_length=200)
     
class funcionarios(models.Model): 
    nome_funcionario = models.CharField('Nomefunc', max_length=100)
    idade = models.IntegerField('Idade')
    cargo = models.CharField('Cargo', max_length=100)

class unidades(models.Model): 
    cidade = models.CharField('Cidade', max_length=100)
    endereco = models.CharField('Endereço', max_length=100)
    numero_funcionarios = models.IntegerField('Número de funcionários')
