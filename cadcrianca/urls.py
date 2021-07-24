from django.urls import path
from .views import ChamdaList, CriancaList, AlunoCreate, AlunoUpdate, AlunoDelete
from .views import *

app_name = "cadcrianca"

urlpatterns = [
    path("cadastro/", CadastroView.as_view(), name="cadastro"),
    path("listar-cadastros/", CriancaList.as_view(), name="listar-cadastros"),
    path("cadastro-form/", AlunoCreate.as_view(), name="form"),
    path("update-form/<int:pk>", AlunoUpdate.as_view(), name="update-aluno"),
    path("delete-form/<int:pk>", AlunoDelete.as_view(), name="delete-aluno"),

    path("chamada/", ChamdaList.as_view(), name='chamada'),
    path('novo_perfil/', novo_perfil, name='novo_perfil'),
]
