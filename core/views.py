from django.shortcuts import render, redirect

from .models import Produtos
from .models import Funcionarios
from .models import Unidades


def listar_produtos(request):
    produto = Produtos.objects.all()
    contexto = {
        'todos_produtos': produto
    }
    return render(request, 'produtos.html', contexto)

def listar_funcionarios(request):
    funcionario = Funcionarios.objects.all()
    contexto = {
        'todos_funcionarios': funcionario
    }
    return render(request, 'funcionarios.html', contexto)  

def listar_unidades(request):
    unidade = Unidades.objects.all()
    contexto = {  
         'todas_unidades': unidade
    }
    return render(request, 'unidades.html', contexto)  
