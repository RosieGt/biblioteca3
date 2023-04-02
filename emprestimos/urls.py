"""vcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from .views import index, realizar_emprestimo_livro, realizar_emprestimo, listar_autor, detalhar_autor, cadastrar_autor, atualizar_autor, deletar_autor, listar_livro, detalhar_livro, cadastrar_livro, atualizar_livro, deletar_livro

urlpatterns = [
    path('', index, name='index'),
    path('livro/emprestimo/<int:livro_pk>', realizar_emprestimo_livro, name='realizar_emprestimo_livro'),
    path('emprestimo/add', realizar_emprestimo, name='realizar_emprestimo'),
    path('autor/', listar_autor, name='listar_autor'),
    path('autor/<int:pk>', detalhar_autor, name='detalhar_autor'),
    path('autor/cadastrar', cadastrar_autor, name='cadastrar_autor'),
    path('autor/atualizar/<int:pk>', atualizar_autor, name='atualizar_autor'),
    path('autor/deletar/<int:pk>', deletar_autor, name='deletar_autor'),
    path('livro/', listar_livro, name='listar_livro'),
    path('livro/<int:pk>', detalhar_livro, name='detalhar_livro'),
    path('livro/cadastrar', cadastrar_livro, name='cadastrar_livro'),
    path('livro/atualizar/<int:pk>', atualizar_livro, name='atualizar_livro'),
    path('livro/deletar/<int:pk>', deletar_livro, name='deletar_livro')
]

