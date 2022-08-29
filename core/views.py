from django.shortcuts import render, redirect
from .models import Cafe
from .forms import CafeForm


def cafe(request):
    produtos = Cafe.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render(request, 'bigs.html', contexto)

def cadastrar_produtos(request):
    form = CafeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('cafe')
    contexto = {
        'form_cafe': form
    }
    return render(request, 'bigs_cadastrar.html', contexto)