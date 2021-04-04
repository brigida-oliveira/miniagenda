from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from tarefas.models import Tarefa

# Create your views here.
@login_required
def home(request):
    tarefas = Tarefa.objects.filter(user=request.user) #SELECT * FROM tarefa; ORM - Object Relationship Manager
    return render(request, 'core/index.html', {'tarefas': tarefas})
