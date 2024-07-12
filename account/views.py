from django.shortcuts import render

# Create your views here.

def addeducation(request):
    return render(request, 'account/addeducation.html' , {})

def addexperience(request):
    return render(request, 'account/addexperience.html' , {})

def creatprofile(request):
    return render(request, 'account/creatprofile.html' , {})

def dashboard(request):
    return render(request, 'account/dashboard.html' , {})

def login(request):
    return render(request, 'account/login.html' , {})

def profile(request):
    return render(request, 'account/profile.html' , {})

def profiles(request):
    return render(request, 'account/profiles.html' , {})

def register(request):
    return render(request, 'account/register.html' , {})
