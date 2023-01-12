from django import forms 
from .models import Abrigo, Pet 

class abrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = {'nome', 'descricao','endereco', 'fotos', 'redes_sociais'}

class petForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = {'nome', 'fotos', 'idade','especie', 'raca', 'sexo', 'abrigo'}