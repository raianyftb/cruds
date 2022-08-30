"""cruds URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
<<<<<<< HEAD
from core.views import listar_produtos, cadastrar_produtos, editar_produtos
=======
from core.views import listar_produtos
from core.views import listar_funcionarios
from core.views import listar_unidades
<<<<<<< HEAD
from core.views import listar_produtos, cadastrar_produtos, cadastrar_funcionarios, cadastrar_unidades
=======
from core.views import listar_produtos, cadastrar_produtos
>>>>>>> 2f842f4e977ffe400ea42cbca70a8dd2c1cdddb9
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40

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
>>>>>>> dcbc159a4c65edca5f1234fbfd05a13c64db4f40
    path('admin/', admin.site.urls),
]
