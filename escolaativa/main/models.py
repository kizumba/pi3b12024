from django.db import models

# Create your models here.
class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    turno_turma = models.CharField(max_length=20)
    ano_turma = models.IntegerField()
    serie_turma = models.CharField(max_length=5)

    def __str__(self):
        return self.id_turma