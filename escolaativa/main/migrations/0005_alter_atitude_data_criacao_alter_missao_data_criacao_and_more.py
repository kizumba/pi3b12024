# Generated by Django 4.2.11 on 2024-04-03 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_turma_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atitude',
            name='data_criacao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='missao',
            name='data_criacao',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='turma',
            name='data_criacao',
            field=models.DateField(auto_now=True),
        ),
    ]
