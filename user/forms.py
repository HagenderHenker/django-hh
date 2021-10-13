from django import forms
from django.forms.fields import CharField, ChoiceField
from hhapp.models import Haushalt



class setsessionhh(forms.Form):
    gemeinde = forms.ChoiceField()
    haushaltsjahr = forms.CharField(max_length=100)
    