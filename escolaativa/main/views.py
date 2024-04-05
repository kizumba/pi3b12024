from django.shortcuts import render

from django.views.generic.edit import FormView

from main import forms

from django.shortcuts import render, get_object_or_404
from .models import Turma

# Create your views here.
class ViewFaleConosco(FormView):
    template_name = "fale_conosco.html"
    form_class = forms.FormFaleConosco
    success_url = "/"

    def form_valid(self, form):
        form.enviar_mensagem_por_email()
        return super().form_valid(form)

def listar_turmas(request, id_turma=None):
        turma = None
        lista_turmas = Turma.objects.all()
        if id_turma:
            turma = get_object_or_404(Turma, id=id_turma)
            #lista_turmas = Turma.objects.filter(turma=turma)
        contexto = {
            'turma':turma,
            'lista_turmas':lista_turmas,
        }
        return render(request, 'turmas/listar.html',contexto)
    
def detalhes_turma(request, id):
    turma = get_object_or_404(Turma, id=id)
    contexto = {
           'turma':turma,
    }
    return render(request, 'turma/detalhes.html',contexto)
