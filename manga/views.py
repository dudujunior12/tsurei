from queue import Empty
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, UploadMangaForm, CreateNewChapter
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Manga, Chapter, Category, Bookmark
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    most_viewed_mangas = Manga.objects.all().order_by("-manga_views")[:10]
    latest_mangas = Manga.objects.filter().order_by("-posted_date")

    
    return render(request, "manga/index.html", {
        "most_viewed_mangas": most_viewed_mangas,
        "latest_mangas": latest_mangas,
        })

def manga_chapter(request, manga_id, chapter_id):
    manga = get_object_or_404(Manga, id=manga_id)
    chapter = Chapter.objects.get(manga=manga, id=chapter_id)
    print(chapter)
    return render(request, "manga/manga_chapter.html", {"chapter": chapter, "manga": manga})

def new_chapter(request, manga_id):
    if request.method == "POST":
        form = CreateNewChapter(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            form = form.save(commit=False)
            form.manga = get_object_or_404(Manga, id=manga_id)
            form.save()
        else:
            print("Chapter Error")
        return redirect("show-manga", id=manga_id)
    else:
        return JsonResponse({"message_error": "Require POST request method"}, status=404)

def latest(request):
    latest_mangas = Manga.objects.filter().order_by("-posted_date")
    return render(request, 'manga/latest.html', {"latest_mangas": latest_mangas})

def categories(request, category):
    categories = Category.objects.all()
    if(category == "All"):
        categories_mangas = Manga.objects.all()
    else:
        category = Category.objects.get(category_name=category).id
        categories_mangas = Manga.objects.filter(category=category)
    return render(request, 'manga/categories.html', {"categories_mangas": categories_mangas, "categories": categories})

@login_required
def profile(request, username):
    other_user = get_object_or_404(User, username=username)
    bookmarked_mangas = get_bookmarked_mangas(other_user)
            
    return render(request, "manga/profile.html", {"bookmarked_mangas": bookmarked_mangas, "username": username})

def search(request):
    if request.method == "GET":
        search_text = request.GET['q']
        mangas = Manga.objects.all()
        result = []
        for manga in mangas:
            if search_text.lower() in manga.title.lower():
                result.append(manga)
            if search_text.lower() == manga.title.lower():
                result.append(manga)
        if len(result) > 0:
            return render(request, "manga/search.html", {"search_text": search_text, "result": result})
        else:
            return render(request, "manga/search.html", {"search_text": search_text, "error": "There were no results matching the query"})
    

def get_bookmarked_mangas(other_user):
    bookmarks = Bookmark.objects.filter(user=other_user)
    bookmarked_mangas = []
    for bookmark in bookmarks:
        bookmarked_manga = Manga.objects.get(title=bookmark.manga.title)
        bookmarked_mangas.append(bookmarked_manga)

    return bookmarked_mangas

@login_required
@csrf_exempt
def add_bookmark(request, manga_id):
    if request.method == "POST":
        manga = Manga.objects.get(id=manga_id)

        if Bookmark.objects.filter(user=request.user, manga=manga):
            Bookmark.objects.get(user=request.user, manga=manga).delete()
            bookmarked = False

            return JsonResponse({"message": "Unbookmarked successfully. ", "bookmarked": bookmarked})
        else:
            Bookmark(user=request.user, manga=manga).save()
            bookmarked = True
            return JsonResponse({"message": "Bookmarked successfully. ", "bookmarked": bookmarked})

    return JsonResponse({"message_error": "POST request required."})

def show_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    print(manga.manga_views)
    manga.manga_views = manga.manga_views + 1
    print(manga.manga_views)
    manga.save()

    new_chapter_form = CreateNewChapter()

    manga_chapters = Chapter.objects.filter(manga=manga)
    try:
        bookmark = Bookmark.objects.filter(user=request.user, manga=manga)

        if bookmark:
            bookmarked = "Bookmarked"
        else:
            bookmarked = "Bookmark"
    except:
        bookmarked = "Bookmark"





    return render(request, "manga/show_manga.html", {
        "manga": manga, 
        "manga_chapters": manga_chapters,
        "new_chapter_form": new_chapter_form,
        "bookmarked": bookmarked,
    })

def get_manga(request, id):
    if request.method == "GET":
        manga = get_object_or_404(Manga, id=id)
        return JsonResponse({"manga_title": manga.title, "manga_summary": manga.summary, "manga_status": manga.status, "manga_author": manga.author, "manga_id": manga.id})
    
    return JsonResponse({"message_error": "Get method required."})

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