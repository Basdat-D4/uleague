from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# Create your views here.
def login_user(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return HttpResponseRedirect("/")

def register_user(request):
    return render(request, 'registration.html', {})

def show_dashboard(request):
    return render(request, 'dashboard_panitia.html')