from django.contrib import admin

from .models import Atitude, Equipe, Missao, Turma

# Register your models here.
@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ['id_turma','serie','periodo','data_criacao']
    list_filter = ['id_turma','serie','periodo','data_criacao']
    list_editable = ['serie','periodo']
    
