<<<<<<< HEAD

from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, cadastrar_produtos, editar_produtos
from core.views import listar_produtos
from core.views import listar_funcionarios
from core.views import listar_unidades
=======
from django.contrib import admin
from django.urls import path
from core.views import listar_produtos, cadastrar_produtos, editar_produtos, remover_produtos
from core.views import listar_produtos
from core.views import listar_funcionarios
from core.views import listar_unidades
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 94ad50d03c3bad1756fea125db6e5247405391fc
from core.views import listar_produtos, cadastrar_produtos, cadastrar_funcionarios, cadastrar_unidades
from core.views import listar_produtos, cadastrar_produtos
<<<<<<< HEAD

=======
>>>>>>> 2f842f4e977ffe400ea42cbca70a8dd2c1cdddb9
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40
>>>>>>> 2abec525562e75bf562ef285dcf8e20879c8af1a
>>>>>>> 94ad50d03c3bad1756fea125db6e5247405391fc

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('funcionarios/', listar_funcionarios, name='listar_funcionarios'),
    path('unidades/', listar_unidades, name='listar_unidades'),
    path('cadastrar_produtos/', cadastrar_produtos, name='cadastrar_produtos'),

    path('cadastrar_funcionarios/', cadastrar_funcionarios, name='cadastrar_funcionarios'),
    path('cadastrar_unidades/', cadastrar_unidades, name='cadastrar_unidades'),
 
    path('editar_produtos/<int:id>/', editar_produtos, name='editar_produtos'),
<<<<<<< HEAD

=======
<<<<<<< HEAD
    path('remover_produtos/<int:id>/', remover_produtos, name='remover_produtos'),
=======
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40
>>>>>>> 2abec525562e75bf562ef285dcf8e20879c8af1a
>>>>>>> 94ad50d03c3bad1756fea125db6e5247405391fc
    path('admin/', admin.site.urls),
]
