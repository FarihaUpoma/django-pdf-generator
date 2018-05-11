from django.shortcuts import render

# Create your views here.
from easy_pdf.views import PDFTemplateView

from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

from django.conf import settings


class HelloPDFView(PDFTemplateView):
    template_name = 'index.html'

