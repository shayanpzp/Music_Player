from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Activate the user
            user.save()
            # login(request, user)  # Temporarily comment out this line for debugging
            return redirect('home')
        else:
            print("Form is not valid")
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})



def sign_in(request):
    pass

def home(request):
    return render(request, 'home.html')
