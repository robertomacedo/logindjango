from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class ListagemView(TemplateView):
    template_name = "listagem.html"


class ListaView(TemplateView):
    template_name = "lista-datails.html"


