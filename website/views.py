from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mysite.models import Funcionario
from mysite.forms import FuncionarioForm
from django.urls import reverse
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.http import Http404



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

def atualizar_funcionario(request, _id):
    try:
        old_data = get_object_or_404(Funcionario, id = _id)
    except Exception:
        raise Http404('Não existe')

    if request.method == 'POST':
        form = FuncionarioForm (request.POST, instance = old_data)

        if form.is_valid():
            form.save()
            return redirect(f'/att/{_id}')

    else:
        form = FuncionarioForm(instance = old_data)
        context ={'form':form}
        return render(request,'atualizar.html',context)

def delete_funcionario(request, _id):
    try:
        data = get_object_or_404(Funcionario, id = _id)
    except Exception:
        raise Http404('Não existe')

    if request.method == 'POST':
        data.delete()
        return redirect('/')
    else:
        return render(request, 'delete.html')