from dataclasses import fields
from pyexpat import model
from django.forms import ModelForm
from .models import Produtos
from .models import Funcionarios
from .models import Unidades

class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields = ['nome', 'tipo', 'marca','quantidade', 'descricao']

class FuncionariosForm(ModelForm):
    class Meta:
        model = Funcionarios
        fields = ['nome_funcionario', 'idade', 'cargo']

class UnidadesForm(ModelForm):
    class Meta:
        model = Unidades
        fields = ['cidade', 'endereco', 'numero_funcionarios']