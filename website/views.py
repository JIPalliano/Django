from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.models import Funcionario
from mysite.forms import FuncionarioForm
from django.urls import reverse
from django.shortcuts import redirect
from django.views.generic import UpdateView


# Create your views here.


def lista_funcionarios(request):

    funcionarios = Funcionario.objetos.all()

    contexto = {'funcionarios': funcionarios}

    return render(request, "funcionarios.html", contexto)


def criar_novo_funcionario(request):

    form = FuncionarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('website:lista_funcionarios')

    return render(request, "form.html", {'form':form})

def FuncionariosUpdateView(resquest, id):
    funcionario = Funcionario.objetos.get(id=id)
    form = Funcionario(request.POST or None, instance=funcionario)

    if form.is_valid():
        form.save()
        return redirect('website:lista_funcionarios')

    return render(request, 'atualizar.html', {'form':form, 'funcionario':funcionario})
    
