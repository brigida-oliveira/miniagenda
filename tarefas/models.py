from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TarefaManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().filter(models.Q(nome__icontains=query) | models.Q(descricao__icontains=query) | models.Q(categoria__nome__icontains=query), user=user)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )

    STATUS_CHOICES = (
        ('C', 'Concluída'),
        ('P', 'Em progresso'),
        ('CD', 'Cancelada'),
    )

    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricao = models.TextField(verbose_name='Descrição', blank=True)
    data_final = models.DateField(verbose_name='Data final')
    prioridade = models.CharField(max_length=1, verbose_name='Prioridade', choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria')
    user = models.ForeignKey(User)
    status = models.CharField(max_length=5, verbose_name='Status', choices=STATUS_CHOICES, blank=True, default='P')

    objects = TarefaManager()

    def __str__(self):
        return self.nome
