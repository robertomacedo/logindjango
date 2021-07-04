from django.urls import path

from . import views
from .views import CriancaList, AlunoCreate, AlunoUpdate, AlunoDelete, PerfilUpdate, ListaDatails

app_name = "cadcrianca"

urlpatterns = [
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
    path("listar-cadastros/", CriancaList.as_view(), name="listar-cadastros"),
    path("cadastro-form/", AlunoCreate.as_view(), name="form"),
    path("update-form/<int:pk>", AlunoUpdate.as_view(), name="update-aluno"),
    path("delete-form/<int:pk>", AlunoDelete.as_view(), name="delete-aluno"),
    path("atualizar-dados/", PerfilUpdate.as_view(), name="atualizar-dados"),
    path("lista-datails/", ListaDatails.as_view(), name="lista-datails"),
]