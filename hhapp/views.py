from django.shortcuts import render, redirect

# Create your views here.

def start(request):
    return render(request, "hhapp/hh.html")


def upload(request):
    if request.method == "POST":
        upload_file = request.FILES['document']
        print(upload_file.name)
        print(upload_file.size)
        return redirect('home')

    else:
        return render(request, "hhapp/upload.html")


    

