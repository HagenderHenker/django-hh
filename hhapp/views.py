from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import Datafile_form
from django.views.generic import ListView

# Create your views here.

def start(request):
    return render(request, "hhapp/hh.html")


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
    pass

def datafile_list(request):
    
    if request.method == "GET":
        form = Datafile_form()
        return render(request, "hhapp/datafile_list.html", {'form': form})    
    
    if request.method == "POST":
        form = Datafile_form(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('home')
    


    

