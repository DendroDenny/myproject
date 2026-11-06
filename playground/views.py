from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here

def home(request):
    return render(request, 'playground/home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if username and password match a database record
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {username}!")
            return redirect('dashboard') # Update 'dashboard' later once you create it
        else:
            messages.error(request, "Invalid username or password.")
            
    return render(request, 'playground/home.html')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now sign in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'playground/register.html', {'form': form})