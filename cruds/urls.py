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
from core.views import listar_produtos, cadastrar_produtos, editar_produtos

urlpatterns = [
    path('produtos/', listar_produtos, name='listar_produtos'),
    path('cadastrar_produtos/', cadastrar_produtos, name='cadastrar_produtos'),
    path('editar_produtos/<int:id>/', editar_produtos, name='editar_produtos'),
    path('admin/', admin.site.urls),
]
