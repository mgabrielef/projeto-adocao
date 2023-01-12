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


class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    fotos = models.ImageField(upload_to='Pet')
    idade = models.IntegerField()
    especie = models.CharField(max_length=20)
    raca = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    abrigo = models.ForeignKey(Abrigo, on_delete=models.CASCADE)

    def str(self):
        return self.nome