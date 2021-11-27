from django.forms import ModelForm
from .models import Datafiles, Haushalt, Steuerkraft, Steuerkraftgrunddaten, Berechnungsgrundlagen

class Datafile_form(ModelForm):
    class Meta:
        model = Datafiles
        fields = ['datafilebez', 'datafile']



'''
Haushaltsgrunddaten Forms
In this Forms the Forms for the "Haushaltsgrunddaten" models are set up
'''

class Haushalt_form(ModelForm):
    class Meta:
        model = Haushalt
        fields ='__all__'
        

'''
Haushaltsstatistik Forms
In the following Forms the forms for the "Haushaltsstatistik" models are set up
'''        
        


'''
KFA Forms
In the following Forms the forms for the "Kommunaler Finanzausgleich" models are set up
'''
        
class KFABerechnungsgrundlagen_form(ModelForm):
    class Meta:
        model = Berechnungsgrundlagen
        fields = '__all__'
        labels = []
    
        
class Steuerkraft_form(ModelForm):
    class Meta:
        model = Steuerkraft
        fields = '__all__'
        
class Steuerkraftgrunddaten_form(ModelForm):
    class Meta:
        model = Steuerkraftgrunddaten
        fields = '__all__'


