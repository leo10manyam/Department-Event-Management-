from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

from app1.forms import RegistrationForm, UserRegistrationForm
from .models import Registration



# Create your views here.
def register(request):
    return render(request,'login.html')
def index(request):
    return render(request,'index.html')
def Appdev(request):
    return render(request,'Appdev.html')
def cquest(request):
    return render(request,'cquest.html')
def home(request):
    return render(request,'index.html')



def register_or_login(request):
    if request.method == 'POST':
        if 'signup' in request.POST:
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, 'Username already exists')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    messages.success(request, f'Account created for {username}!')
                    return redirect('login')
            else:
                messages.error(request, 'Passwords do not match')
        elif 'signin' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Welcome back, {username}!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid username or password')

    return render(request, 'register_or_login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('login')




def appdev_reg(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('App')  # Redirect to avoid resubmission
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = RegistrationForm()
    
    return render(request, 'appdev_reg.html', {'form': form})

def registers(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login1.html', {'error': 'Invalid credentials'})
    return render(request, 'login1.html')
