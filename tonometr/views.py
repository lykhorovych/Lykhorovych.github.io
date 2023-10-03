from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Tonometr
from .forms import TonometrForm


def index(request):
    return render(request, template_name='tonometr/base.html')
# Create your views here.
class AddTon(CreateView):
    model = Tonometr
    form_class = TonometrForm
    template_name = 'tonometr/add.html'
    success_url = reverse_lazy('base')


class ListTon(ListView):
    model = Tonometr
    template_name = 'tonometr/all.html'