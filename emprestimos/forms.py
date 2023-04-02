from django.forms import ModelForm
from .models import Emprestimo, Autor, Livro, Perfil
from django.contrib.auth.forms import UserCreationForm

class EmprestimoForm(ModelForm):
    class Meta:
        model = Emprestimo
        fields = '__all__'

class AutorForm(ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'

class LivroForm(ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'      

class MyUserCreationForm(UserCreationForm):
    pass
          
               