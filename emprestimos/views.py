from django.shortcuts import render, redirect
from .models import Autor, Livro, Emprestimo, Perfil
from django.contrib.auth.decorators import login_required
from .forms import EmprestimoForm, AutorForm, LivroForm, MyUserCreationForm



# Create your views here.
def index(request):
    livros = Livro.objects.all()[:5]
    autores = Autor.objects.all()[:5]
    return render(request, 'index.html', { 'autores':autores, 'livros':livros})


def realizar_emprestimo(request):
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = EmprestimoForm()
            return render(request, "emprestimo/cadastrar.html", {'form': form})
    else:
        form = EmprestimoForm()
        return render(request, "emprestimo/cadastrar.html", {'form': form})

def realizar_emprestimo_livro(request, livro_pk):
    livro = Livro.objects.get(pk=livro_pk)
    emprestimo = Emprestimo()
    emprestimo.livro = livro
    
    form = EmprestimoForm(instance=emprestimo)
    if request.method == "POST":
        form = EmprestimoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = EmprestimoForm(instance=emprestimo)
            return render(request, "emprestimo/cadastrar.html", {'form': form})
    else:
        form = EmprestimoForm(instance=emprestimo)
        return render(request, "emprestimo/cadastrar.html", {'form': form})

def listar_autor(request):
    autores = Autor.objects.all()
    context = {"autores": autores}
    return render(request, "autor/listar.html", context)

def detalhar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    context = {"autor": autor}
    return render(request, "autor/detalhar.html", context)

@login_required
def cadastrar_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = AutorForm()
            return render(request, "autor/cadastrar.html", {'form': form})
    else:
        form = AutorForm()
        return render(request, "autor/cadastrar.html", {'form': form})

def atualizar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)
    form = AutorForm(instance=autor)
    
    if request.method == "POST":
        form = AutorForm(request.POST, request.FILES, instance=autor)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "autor/atualizar.html", {'form': form})
    else:
        return render(request, "autor/atualizar.html", {'form': form})

def deletar_autor(request, pk):
    autor = Autor.objects.get(pk=pk)

    if autor:
        autor.delete()
        return redirect("/")
    else:
        return render(request, "autor/listar.html", {'msg': "Autor não encontrado"})

def detalhar_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    context = {"livro": livro}
    return render(request, "livro/detalhar.html", context)

def listar_livro(request):
    livros = Livro.objects.all()
    context = {"livros": livros}
    return render(request, "livro/listar.html", context)

@login_required
def cadastrar_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = LivroForm()
            return render(request, "livro/cadastrar.html", {'form': form})
    else:
        form = LivroForm()
        return render(request, "livro/cadastrar.html", {'form': form})

def atualizar_livro(request, pk):
    livro = Livro.objects.get(pk=pk)
    form = LivroForm(instance=livro)
    
    if request.method == "POST":
        form = LivroForm(request.POST, request.FILES, instance=livro)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request, "livro/atualizar.html", {'form': form})
    else:
        return render(request, "livro/atualizar.html", {'form': form})

def deletar_livro(request, pk):
    livro = Livro.objects.get(pk=pk)

    if livro:
        livro.delete()
        return redirect("livro/listar")
    else:
        return render(request, "livro/listar.html", {'msg': "livro não encontrado"})        
    
def registration(request):
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            form = MyUserCreationForm()
            return render(request, "registration/registration.html", {'form': form})
    else:
        form = MyUserCreationForm()
        return render(request, "registration/registration.html", {'form': form})