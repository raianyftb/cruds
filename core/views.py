from django.shortcuts import render, redirect
from .models import Produtos
from .models import Funcionarios
from .models import Unidades

from .forms import ProdutosForm
from .forms import FuncionariosForm
from .forms import UnidadesForm


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
    form = FuncionariosForm(request.POST or None)  
    if form.is_valid():
        form.save()
        return redirect('listar_funcionarios')
    
    contexto = {
        'form_funcionarios': form
    }
    
    return render(request, 'funcionarios_cadastrar.html')

def cadastrar_unidades(request):
    form = UnidadesForm(request.POST or None) 
    if form.is_valid():
        form.save()
        return redirect('listar_unidades') 
    contexto = {
        'form_unidades': form
    }
    
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

def editar_funcionarios(request, id):
    return render(request, 'curso_cadastrar.html')


def editar_unidades(request, id):
    return render(request, 'curso_unidades.html')




def remover_produtos(request,id):
    produto = Produtos.objects.get(pk=id)
    produto.delete()
    return redirect('listar_produtos')
