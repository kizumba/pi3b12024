# Generated by Django 4.2.11 on 2024-03-31 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id_turma', models.AutoField(primary_key=True, serialize=False)),
                ('turno_turma', models.CharField(max_length=20)),
                ('ano_turma', models.IntegerField()),
                ('serie_turma', models.CharField(max_length=5)),
            ],
        ),
    ]