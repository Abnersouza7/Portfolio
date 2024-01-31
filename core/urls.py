from django.urls import path
from .views import *

urlpatterns = [
    path("", HomeTemplateView.as_view(), name="home"),
    path(
        "trajetoria_pessoal/",
        TrajetoriaPessoalTemplateView.as_view(),
        name="trajetoria_pessoal",
    ),
    path(
        "trajetoria_profissional/",
        TrajetoriaProfissionalTemplateView.as_view(),
        name="trajetoria_profissional",
    ),
    path("certificates/", CertificateListView.as_view(), name="view_certificates"),
]
