from django.shortcuts import render
from .forms import CreateUserForm
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.
def index(request):
    return render(request, "manga/index.html", {})

def login(request):
    form = AuthenticationForm()
    return render(request, "manga/login.html", {"form": form})

def register(request):
    form = CreateUserForm()
    return render(request, "manga/register.html", {"form": form})