from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, UploadMangaForm, CreateComment
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Manga, Chapter, Comment
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def index(request):
    popular_mangas = Manga.objects.all()
    most_viewed_mangas = Manga.objects.all()
    latest_mangas = Manga.objects.all()

    print(latest_mangas.first().chapters.first().chapter_number)

    return render(request, "manga/index.html", {
        "popular_mangas": popular_mangas,
        "most_viewed_mangas": most_viewed_mangas,
        "latest_mangas": latest_mangas,
        })

@login_required
@csrf_exempt
def edit_comment(request, manga_id, comment_id):
    if request.method == "POST":
        user = request.user
        comment = get_object_or_404(Comment, id=comment_id, user=user)
        data = json.loads(request.body)
        if data.get("comment_text") is not None:
            comment.comment_text = data["comment_text"]
        comment.save()

        return JsonResponse({"message": "Comment edited successfully.", "comment_text": comment.comment_text}, status=201)
    else:
        return JsonResponse({"message_error": "Require POST request method."}, status=404)

@login_required
def new_comment(request, id):
    if request.method == "POST":
        form = CreateComment(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.manga = get_object_or_404(Manga, id=id)
            form.save()
        return redirect("show_manga", id=id)
    else:
        return JsonResponse({"message_error": "Require POST request method"}, status=404)

def show_manga(request, id):
    comment_form = CreateComment()

    
    # Bookmark 

    # Add Chapter

    # Create Comment

    # Follow

    # Profile

    manga = get_object_or_404(Manga, id=id)
    manga_chapters = Chapter.objects.filter(manga=manga)
    comments = Comment.objects.filter(manga=manga).order_by("-posted_date")

    return render(request, "manga/show_manga.html", {"manga": manga, "manga_chapters": manga_chapters, "comment_form": comment_form, "comments": comments})

def get_manga(request, id):
    if request.method == "GET":
        manga = get_object_or_404(Manga, id=id)
        return JsonResponse({"manga_title": manga.manga_title, "manga_summary": manga.summary, "manga_status": manga.status, "manga_author": manga.author, "manga_id": manga.id})
    
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