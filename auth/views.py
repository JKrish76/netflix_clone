from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.
def home(request):
    return render(request, 'auth/index.html')

def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        

        myuser = User.objects.create_user(username, password, email)
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('login')
        myuser.password = password
        myuser.email = email
        myuser.save()

        messages.success(request, "User created successfully!")
        return redirect('login')

    return render(request, 'auth/signup.html')

def login(request):
    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            usser = user.username
            return render(request, 'auth/index.html', {'username': usser})
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('home')

    return render(request, 'auth/login.html')

def signout(request):
    pass