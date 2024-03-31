from django.db import models

# Create your models here.
class Turma(models.Model):
    id_turma = models.AutoField(primary_key=True)
    serie = models.CharField(max_length=10)
    periodo = models.CharField(max_length=15)
    data_criacao = models.DateField()

    def __str__(self):
        return f'Turma: Série: {self.serie}, período: {self.periodo} criada em {self.data_criacao}'