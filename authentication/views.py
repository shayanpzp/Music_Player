from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page or other appropriate page
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def sign_in(request):
    pass

def home(request):
    return render(request, 'home.html')
