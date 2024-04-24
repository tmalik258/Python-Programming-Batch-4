from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .forms import SignUpForm

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
    if request.method == 'POST':
        pass
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {
        'form': form
    })


def logoutView(request):
    logout(request)
    return redirect('index')

