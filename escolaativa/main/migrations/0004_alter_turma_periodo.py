# Generated by Django 4.2.11 on 2024-04-02 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_equipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='turma',
            name='periodo',
            field=models.CharField(choices=[('M', 'Manhã'), ('T', 'Tarde'), ('N', 'Noite')], max_length=1),
        ),
    ]
