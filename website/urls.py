
from django.contrib import admin
from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [

    path('', views.lista_funcionarios, name='lista_funcionarios' ),

    path('new/', views.criar_novo_funcionario, name="novo"),

    path('att/<int:_id>/atualizar/', views.atualizar_funcionario, name='editar'),

    path('delete/<int:_id>/delete/', views.delete_funcionario, name='deletar'),

]
