from django.shortcuts import render, redirect

from .models import Produtos


def listar_produtos(request):
    produto = Produtos.objects.all()
    contexto = {
        'todos_produtos': produto
    }
    return render(request, 'produtos.html', contexto)

def cadastrar_produtos(request):
    return render(request, 'produtos_cadastrar.html')