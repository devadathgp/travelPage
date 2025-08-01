
from . models import *
from django import forms

class TravelPageForm(forms.ModelForm):
    class Meta:
        model=TravelPage
        fields='__all__'