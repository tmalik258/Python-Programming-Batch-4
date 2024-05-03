from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from .forms import SignUpForm

# Create your views here.

def loginView(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.info(request, 'You are Logged In Successfully!')
            return redirect('index')
        else:
            return redirect('login')

    return render(request, 'accounts/login.html')


def signUpView(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect('index')
        
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {
        'form': form
    })


def logoutView(request):
    logout(request)
    return redirect('index')

