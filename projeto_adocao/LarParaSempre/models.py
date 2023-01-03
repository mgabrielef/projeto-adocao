from django.db import models

# Create your models here.
class Abrigo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.TextField()
    fotos = models.ImageField(upload_to='Abrigo')
    endereco = models.CharField(max_length=100)
    redes_sociais = models.CharField(max_length=100)

    def str(self):
        return self.nome
