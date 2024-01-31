from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.clickjacking import xframe_options_exempt
from .models import *


class HomeTemplateView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = About.objects.all()
        return context


class TrajetoriaPessoalTemplateView(TemplateView):
    template_name = "trajetoria_pessoal.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trajetorias"] = trajetoria_pessoal.objects.all()
        return context


class TrajetoriaProfissionalTemplateView(TemplateView):
    template_name = "trajetoria_profissional.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["trajetoria_profissional"] = trajetoria_profissional.objects.all()
        return context


class CertificateListView(TemplateView):
    template_name = "certificates.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["certificates"] = Certificate.objects.all()
        return context
