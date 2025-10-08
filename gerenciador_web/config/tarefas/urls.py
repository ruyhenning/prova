from django.urls import path
from . import views
urlpatterns = [
  
    path('',views.listar_tarefas, name='listar_tarefas'),
    path('<int:tarefa_id>/', views.detalhe_tarefa ,name = "detalhe_tarefa"),

    path('adicionar/', views.adicionar_tarefa, name = 'adicionar_tarefa'),


 ]