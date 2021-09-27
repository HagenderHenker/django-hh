from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'user/home.html')

def signup(request):
    return render(request, 'user/signup.html')

def login(request):
    return render(request, 'user/login.html')

def logout(request):
    return render(request, 'user/logout.html')