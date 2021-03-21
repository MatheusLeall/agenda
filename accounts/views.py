from django.shortcuts import render
from django.contrib import messages

def login(request):
    return render(request, 'accounts/login.html')


def logout(request):
    return render(request, 'accounts/logout.html')


def signup(request):
    print(request.POST)
    return render(request, 'accounts/signup.html')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')
