from django.urls import path

from . import views

app_name = "pages"

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home"),
    path("listagem/", views.ListagemView.as_view(), name="listagem"),
    path("lista/", views.ListaView.as_view(), name="lista"),
]