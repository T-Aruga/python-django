from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView

class IndexView(TemplateView):
    template_name = 'tabelogapp/index.html'

def Search(request):
    params = {
    }
    return render (request, 'tabelogapp/index.html', params)
