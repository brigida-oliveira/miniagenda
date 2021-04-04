from django import forms
from .models import Categoria, Tarefa

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ('user',)

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ('user',)

    def __init__(self, user=None, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['categoria'].queryset = Categoria.objects.filter(user=user)
            self.fields['data_final'].widget.attrs['placeholder'] = 'Digite a data nesse formato: dd/mm/aaaa'
