from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import User
from .forms import CustomUserCreationForm
from django.contrib import messages

# Create your views here

def home(request):
    return render(request, 'playground/home.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user_obj = User.objects.get(email=email)
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome back, {user_obj.username}!")
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid email or password.")
                
        except User.DoesNotExist:
            messages.error(request, "Invalid email or password.")
            
    return render(request, 'playground/home.html')

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now sign in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'playground/register.html', {'form': form})