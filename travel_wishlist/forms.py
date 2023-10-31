from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        field = ('name', 'visited')