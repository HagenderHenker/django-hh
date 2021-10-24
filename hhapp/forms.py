from django.forms import ModelForm
from .models import Datafiles

class Datafile_form(ModelForm):
    class Meta:
        model = Datafiles
        fields = ['datafilebez', 'datafile']
        
    
