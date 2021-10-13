from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from hhapp.models import Haushalt


# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def signup(request):
    return render(request, 'user/usersignup.html')

def userlogin(request):
    if request.method == "GET":
        return render(request, 'user/userlogin.html', {'form' : AuthenticationForm()})
    elif request.method == "POST":
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'user/userlogin.html', {'form' : AuthenticationForm(), 'error' : 'Fehler beim Login. Haben Sie das richtige Passwort verwendet?'})
        else:
            login(request, user)
            return redirect('home')

def userlogout(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'user/userlogout.html')

    elif request == 'GET':
        return HttpResponse("GetRequest")
    
    else:
        print("fuck you cheater")
        return HttpResponse("fuck you cheater")

def usersetsessionhh(request):
    
    if request.method == 'POST':
        request.session['hh'] = request.POST['hh-id']
        request.session['hhgemeinde'] = request.POST['hh-gemeinde']
        request.session['hhjahr'] = request.POST['hh-jahr']
        request.session['hhnt'] = request.POST['hh-nt']
        
        print(list(request))
        return redirect('home')
    else:
        hhliste = Haushalt.objects.all()
        context = { 'liste' : hhliste}
        return render(request, 'user/hhauswahl.html', context)


    