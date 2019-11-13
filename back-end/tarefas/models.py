from django.db import models

class Tarefas(models.Model):
    titulo = models.CharField(max_length=100)
    concluido = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo+'-'+self.concluido