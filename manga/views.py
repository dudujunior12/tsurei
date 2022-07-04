from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import CreateUserForm, UploadMangaForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Manga
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    popular_mangas = Manga.objects.all()
    most_viewed_mangas = Manga.objects.all()
    latest_mangas = Manga.objects.all()
    
    return render(request, "manga/index.html", {
        "popular_mangas": popular_mangas,
        "most_viewed_mangas": most_viewed_mangas,
        "latest_mangas": latest_mangas,
        })

@login_required
def upload(request):
    manga_form = UploadMangaForm()
    if request.method == "POST":
        manga_form = UploadMangaForm(request.POST, request.FILES)
        if manga_form.is_valid():
            manga = manga_form.save(commit=False)
            manga.user = request.user
            manga.save()
        else:
            print("MANGA ERRO")

    return render(request, "manga/upload_manga.html", {"manga_form": manga_form})

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