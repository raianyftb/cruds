from django.shortcuts import render, redirect
from .models import Produtos
from .models import Funcionarios
from .models import Unidades

from .forms import ProdutosForm


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

def cadastrar_produtos(request):
    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produtos': form
    }
    return render(request, 'produtos_cadastrar.html', contexto)

def cadastrar_funcionarios(request):
    return render(request, 'funcionarios_cadastrar.html')

def cadastrar_unidades(request):
    return render(request, 'unidades_cadastrar.html')

def editar_produtos(request, id):
    produto = Produtos.objects.get(pk=id)

    form = ProdutosForm(request.POST or None, instace=produto)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')

    contexto = {
        'form_produtos': form 
    }
    return render(request, 'produtos_cadastrar.html')
