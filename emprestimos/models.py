from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Autor(models.Model):

    nome = models.CharField("Nome", max_length=250)
    email = models.EmailField("Email")
    data_cadastro = models.DateField("Data de cadastro")
    
    
    
    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Autores"

class Livro(models.Model):

    titulo = models.CharField("Titulo", max_length=100, null=True)
    descricao = models.CharField("Descrição", max_length=100, null=True)
    editora = models.CharField("Editora", max_length=100, null=True)
    status = models.CharField("Status", max_length=100, null=True)
    img = models.ImageField("Imagem", upload_to='imagens', null=True, blank=True)
    data_cadastro= models.DateField("Data de cadastro")
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livros', verbose_name="Autor", null=True)

    def __str__(self):
        return "{} - {}".format(self.titulo, self.titulo)

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

class Emprestimo(models.Model):

    codigo = models.CharField("Código", max_length=100)
    data_emprestimo = models.DateField("Data de emprestimo")
    data_devolucao = models.DateField("Data de devolução")
    devolucao = models.BooleanField("Devolvido")
    livro = models.ForeignKey(Livro, on_delete=models.DO_NOTHING, related_name='livros_emprestimo', verbose_name="livro", null=True)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name='livro', verbose_name="Autor", null=True) 
    
    def __str__(self):
        return "{} - {} - {}".format(self.codigo, self.usuario.nome, self.livro.titulo,self.livro.autor)

    class Meta:
        verbose_name = "Emprestimo"
        verbose_name_plural = "Emprestimos"
        
class Perfil(models.Model):

    nome_completo = models.CharField("Nome", max_length=250, null=True)
    email = models.EmailField("Email")
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return "{}".format(self.nome)
    
    class Meta:
        verbose_name_plural = "Perfis"
       