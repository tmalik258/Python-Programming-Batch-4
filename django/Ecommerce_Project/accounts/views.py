from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate


# Create your views here.

def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html')


def signUpView(request):
    return render(request, 'accounts/signup.html')


def logoutView(request):
    logout(request)
    return redirect('index')
