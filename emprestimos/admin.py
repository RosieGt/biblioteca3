from django.contrib import admin
from .models import Autor, Livro, Emprestimo, Perfil
# Register your models here.

admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(Perfil)
admin.site.register(Emprestimo)
