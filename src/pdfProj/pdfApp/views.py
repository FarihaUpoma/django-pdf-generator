from django.shortcuts import render

# Create your views here.
from easy_pdf.views import PDFTemplateView

from easy_pdf.views import PDFTemplateResponseMixin
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model

from django.conf import settings


class HelloPDFView(PDFTemplateView):
    template_name = 'pdf_template.html'

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML

def html_to_pdf_view(request):
    paragraphs = ['first paragraph', 'second paragraph', 'third paragraph']
    html_string = render_to_string('core/pdf_template.html', {'paragraphs': paragraphs})

    html = HTML(string=html_string)
    html.write_pdf(target='/tmp/mypdf.pdf');

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response

    return response