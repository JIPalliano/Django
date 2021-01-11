from django import forms
from .models import Funcionario

class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['id','nome', 'sobrenome', 'cpf', 'tempo_de_servico', 'remuneracao' ]