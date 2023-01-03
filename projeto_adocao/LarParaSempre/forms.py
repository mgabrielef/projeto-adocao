from django import forms 
from .models import Abrigo 

class abrigoForm(forms.ModelForm):
    class Meta:
        model = Abrigo
        fields = {'nome', 'descricao','endereco', 'fotos', 'redes_sociais'}
