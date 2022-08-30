from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Produtos
from .models import funcionarios
from .models import unidades

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'tipo', 'marca','quantidade', 'descricao']

class funcionariosForm(ModelForm):
    class Meta:
        model = funcionarios
        fields = ['nome_funcionario', 'idade', 'cargo']

class unidadesForm(ModelForm):
    class Meta:
        model = unidades
        fields = ['cidade', 'endereco', 'numero_funcionarios']
