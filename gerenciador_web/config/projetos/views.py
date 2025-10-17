from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto

def listar_projetos(request):
    # 1. a busca no banco de dados continua a mesma
    projetos_salvos = Projeto.objects.all()

    # 2. criamos um "dicionario do contexto" para enviar os dados ao template.
    # A chave 'minhas_tarefas' será a variável que usaremos no html.
    contexto = {
        'meus_projetos': projetos_salvos
    }

    # 3. renderizamos o tamplate, passando a requisição e o contexto com os dados.
    return render(request, 'projetos/lista.html', contexto)


