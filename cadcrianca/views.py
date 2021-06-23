from django.shortcuts import render
from django.views.generic import TemplateView
from .models import CadastroCrianca


def cadastroview(request):
    data = CadastroCrianca.objects.all()
    return render(request, 'listagem.html', {'data':data})


class CadastroView(TemplateView):
    template_name = "cadastro.html"

class ListagemView(TemplateView):
    template_name = "listagem.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['DATA'] = CadastroCrianca.objects.all()

        return context





