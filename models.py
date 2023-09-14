from django.db import models

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    diretor = models.CharField(max_length=100)
    ano = models.IntegerField()

    def __str__(self):
        return self.titulo
