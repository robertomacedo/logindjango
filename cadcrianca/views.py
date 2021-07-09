from cadcrianca.forms import PerfilForm
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from .models import CadastroCrianca, Perfil
from django.views.generic.list import ListView


from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


def cadastroview(request):
    data = CadastroCrianca.objects.all()
    return render(request, 'listagem.html', {'data': data})


class CadastroView(TemplateView):
    template_name = "form.html"


class ListaDatails(TemplateView):
    template_name = "lista-datails.html"


class ListagemView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('account_login')
    template_name = "listagem.html"


class CriancaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('account_login')
    model = CadastroCrianca
    template_name = 'listar-cadastros.html'

#  Create forms de cdastro de alunos


class AlunoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('account_login')
    model = CadastroCrianca
    fields = ['name', 'phone', 'address', 'data_nascimento', 'mae', 'pai']
    template_name = 'form.html'
    success_url = reverse_lazy('cadcrianca:listar-cadastros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Cadastrar novo aluno"
        context['botao'] = "Cadastrar"
        return context


class AlunoUpdate(UpdateView):
    model = CadastroCrianca
    fields = ['name', 'phone', 'address', 'data_nascimento', 'mae', 'pai']
    template_name = 'form.html'
    success_url = reverse_lazy('cadcrianca:listar-cadastros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Atualizar dados do aluno"
        context['botao'] = "Salvar"
        return context


class AlunoDelete(DeleteView):
    model = CadastroCrianca
    template_name = 'delete-form.html'
    success_url = reverse_lazy('cadcrianca:listar-cadastros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = "Deletar registro do aluno"
        context['botao'] = "Deletar"
        return context


class PerfilUpdate(TemplateView):
    template_name = 'atualizar-dados.html'
    models = Perfil
    fields = ['name_completo', 'cpf', 'telefone', 'email', 'usuario']
    success_url = reverse_lazy('cadcrianca:listar-cadastros')

    def get_object(self, queryset=None):
        self.object = get_object_or_404(Perfil)
        return self.object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['titulo'] = 'Meus dados pessoais'
        context['botao'] = 'Atualizar'

        return context


def perfilsettings(request):
    user = request.user
    form = PerfilForm(istance=user)
    context = {
        'form': form
    }
    return render(request, 'atualizar-dados.html', context)


def upload(request):
    if request.method == 'POST':
        filetitle = request.POST['filetitle']
        uploadfile = request.FILES['uploadfile']

        document = models.Perfil(
            title = filetitle,
            uploadfile = uploadfile
        )
        document.save()

        document = models.Perfil.objects.all()

        return render(request, 'lista-datails.html', context={'files': document})

# lista de chamada


class ChamdaList(LoginRequiredMixin, ListView):  # Carrega dados completos de todos alunos cadastrados
    model = CadastroCrianca
    template_name = 'chamada.html'
