from django.http import HttpResponse
from django.views.generic import TemplateView

class HelloWorldView(TemplateView):
    template_name = 'hello.html'
