from django.urls import path
from . import views
from .views import ChamdaList, CriancaList, AlunoCreate, AlunoUpdate, AlunoDelete

app_name = "cadcrianca"

urlpatterns = [
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
    path("listar-cadastros/", CriancaList.as_view(), name="listar-cadastros"),
    path("cadastro-form/", AlunoCreate.as_view(), name="form"),
    path("update-form/<int:pk>", AlunoUpdate.as_view(), name="update-aluno"),
    path("delete-form/<int:pk>", AlunoDelete.as_view(), name="delete-aluno"),

    path("chamada/", ChamdaList.as_view(), name='chamada'),
    path('novo_perfil/', views.novo_perfil, name='novo_perfil'),
    path("editar-perfil/<int:p_id>", views.editar_p, name="editar-perfil"),
]
