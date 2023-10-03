from django.forms import ModelForm

from .models import Tonometr

class TonometrForm(ModelForm):
    class Meta:
        model = Tonometr
        fields = '__all__'