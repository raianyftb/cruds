from django.shortcuts import render
from .models import Cafe


def cafe(request):
    produtos = Cafe.objects.all()
    contexto = {
        'todos_produtos': produtos
    }
    return render(request, 'bigs.html', contexto)