from django.views.generic import CreateView, TemplateView
from .models import Client
from django.urls import reverse_lazy


class CreateViewUser(CreateView):
    model = Client
    template_name = 'register.html'
    fields = ['first_name', 'last_name', 'phone']
    success_url = reverse_lazy('congrats')


class Index(TemplateView):
    template_name = 'index.html'


class Congratulations(TemplateView):
    template_name = 'congrats.html'
