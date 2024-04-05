from django.urls import path
from .import views
from django.views.generic import TemplateView

app_name='main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('turmas/',views.listar_turmas, name='listar_turmas'),
    path('turma/ <int:id>', views.detalhes_turma,name='detalhes_turma'),
]