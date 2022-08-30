from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, cadastrar_produtos, editar_produtos, remover_produtos
from core.views import listar_produtos
from core.views import listar_funcionarios
from core.views import listar_unidades
<<<<<<< HEAD
=======
<<<<<<< HEAD
from core.views import listar_produtos, cadastrar_produtos, cadastrar_funcionarios, cadastrar_unidades
=======
from core.views import listar_produtos, cadastrar_produtos
>>>>>>> 2f842f4e977ffe400ea42cbca70a8dd2c1cdddb9
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40
>>>>>>> 2abec525562e75bf562ef285dcf8e20879c8af1a

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('unidades/', listar_unidades, name='listar_unidades'),
    path('cadastrar_produtos/', cadastrar_produtos, name='cadastrar_produtos'),
<<<<<<< HEAD
    path('cadastrar_funcionarios/', cadastrar_funcionarios, name='cadastrar_funcionarios'),
    path('cadastrar_unidades/', cadastrar_unidades, name='cadastrar_unidades'),
=======
    path('editar_produtos/<int:id>/', editar_produtos, name='editar_produtos'),
<<<<<<< HEAD
    path('remover_produtos/<int:id>/', remover_produtos, name='remover_produtos'),
=======
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40
>>>>>>> 2abec525562e75bf562ef285dcf8e20879c8af1a
    path('admin/', admin.site.urls),
]
