from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, cadastrar_produtos, editar_produtos, remover_produtos
from core.views import listar_produtos
from core.views import listar_funcionarios
from core.views import listar_unidades

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('unidades/', listar_unidades, name='listar_unidades'),
    path('cadastrar_produtos/', cadastrar_produtos, name='cadastrar_produtos'),
    path('editar_produtos/<int:id>/', editar_produtos, name='editar_produtos'),
    path('remover_produtos/<int:id>/', remover_produtos, name='remover_produtos'),
    path('admin/', admin.site.urls),
]
