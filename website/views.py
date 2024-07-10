from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def home(request):
    
    context = {}
    return render(request, 'website_home.html', context)

def login_user(request):
    pass

def logout_user(request):
    pass