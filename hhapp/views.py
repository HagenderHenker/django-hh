from django.shortcuts import render, redirect, HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from .models import Datafiles, Haushalt
from .forms import Datafile_form, KFABerechnungsgrundlagen_form, Steuerkraftgrunddaten_form, Steuerkraft_form
from django.views.generic import ListView

# Create your views here.

def start(request):
    return render(request, "hhapp/hh.html")

# Steuerungseinträge

def upload(request):
    # if request.method == "POST":
    #     upload_file = request.FILES['document']
    #     fs = FileSystemStorage()
    #     fs.save(upload_file.name, upload_file)
      
        
        
    #     return redirect('home')

    # else:
    #     return render(request, "hhapp/upload.html")
    if request.method == "GET":
        form = Datafile_form()
        return render(request, "hhapp/datafile_list.html", {'form': form})    
    
    if request.method == "POST":
        form = Datafile_form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')


class datafile_listview(ListView):
    model = Datafiles
    template_name = 'hhapp/datafile_list.html'
    context_object_name = 'datafiles'
    
    def post(self, request, *args, **kwargs):
        print(request.__dict__)
        request.session["datafile"] = request._post["pk"]
        request.session["datafilebez"] = request._post["dfbez"]
        return redirect('home')


def datafile_list(request):
    
    if request.method == "GET":
        form = Datafile_form()
        return render(request, "hhapp/datafile_list.html", {'form': form})    
    
    if request.method == "POST":
        form = Datafile_form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')

# Haushaltsgrunddaten

def haushaltsgrunddaten(request):
    
    if request.method == "GET":
        gde = request.session["hhgdenr"] 
        jahr = request.session["hhjahr"]       
        hhliste = Haushalt.objects.filter(gemeinde__exact=gde).filter(haushaltsjahr__exact=jahr)
        context = { 'liste' : hhliste}
        return render(request, 'hhapp/hhauswahl.html', context)
    
    


# Kommunaler Finanzausgleich

def kfagrunddaten(request):
    if request.method == "GET":
        gde = request.session["hhgdenr"] 
        jahr = request.session["hhjahr"]       
        kfagrunddaten = Haushalt.objects.filter(haushaltsjahr__exact=jahr)
        #if kfagrunddaten:
        kfagrunddaten_form = KFABerechnungsgrundlagen_form()
            
            
        context = {"form":kfagrunddaten_form}
        return render(request, 'hhapp/kfagrunddaten.html', context)
    
    if request.method == "POST":
        form = KFABerechnungsgrundlagen_form(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('home')


# 
    


    

