from django.shortcuts import render, redirect
from .models import Produtos
from .forms import ProdutosForm

def listar_produtos(request):
    produto = Produtos.objects.all()
    contexto = {
        'todos_produtos': produto
    }
    return render(request, 'produtos.html', contexto)

def cadastrar_produtos(request):
    form = ProdutosForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('listar_produtos')
        
    contexto = {
        'form_produtos': form
    }
    return render(request, 'produtos_cadastrar.html', contexto)