from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, listar_funcionarios, listar_unidades 
from core.views import cadastrar_produtos, cadastrar_funcionarios, cadastrar_unidades
from core.views import editar_produtos, editar_funcionarios, editar_unidades
from core.views import remover_produtos, remover_unidades, remover_funcionarios, bigs_principal
from django.contrib import admin

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('unidades/', listar_unidades, name='listar_unidades'),
    path('bigs/', bigs_principal, name='bigs_principal'),
    
    path('cadastrar_produtos/', cadastrar_produtos, name='cadastrar_produtos'),
    path('cadastrar_funcionarios/', cadastrar_funcionarios, name='cadastrar_funcionarios'),
    path('cadastrar_unidades/', cadastrar_unidades, name='cadastrar_unidades'),
 
    path('editar_produtos/<int:id>/', editar_produtos, name='editar_produtos'),
    path('editar_funcionarios/<int:id>/', editar_funcionarios, name='editar_funcionarios'),
    path('editar_unidades/<int:id>/', editar_unidades, name='editar_unidades'),
    
    path('remover_produtos/<int:id>/', remover_produtos, name='remover_produtos'),
    path('remover_funcionarios/<int:id>/', remover_funcionarios, name='remover_funcionarios'),
    path('remover_unidades/<int:id>/', remover_unidades, name='remover_unidades'),
    path('admin/', admin.site.urls),
]
