from django import forms
from .models import *

class cadProdForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = '__all__'
