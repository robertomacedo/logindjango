from django.urls import path

from . import views

app_name = "cadcrianca"

urlpatterns = [
    path("cadastro/", views.CadastroView.as_view(), name="cadastro"),
]