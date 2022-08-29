from django.forms import ModelForm
from .models import Cafe

class CafeForm(ModelForm):
    class Meta:
        model =  Cafe
        fields = ['marca', 'tipo', 'quantidade']

        