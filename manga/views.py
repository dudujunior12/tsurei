from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, "manga/index.html", {})

def login_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return redirect('login')
        else:
            print(request.POST)

    return render(request, "manga/login.html", {"form": form})

def register_view(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Password too short")
            return redirect("register")
    
    return render(request, "manga/register.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect("index")