from django.forms import ModelForm
from .models import Datafiles, Haushalt

class Datafile_form(ModelForm):
    class Meta:
        model = Datafiles
        fields = ['datafilebez', 'datafile']
        
class Haushalt_form(ModelForm):
    class Meta:
        model = Haushalt
        fields ='__all__'
        
    
