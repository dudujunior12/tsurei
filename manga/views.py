from queue import Empty
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateUserForm, UploadMangaForm, CreateComment, CreateNewChapter
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Manga, Chapter, Comment, Like, Bookmark, Follow
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

def bookmarks(request):
    other_user = get_object_or_404(User, username=request.user.username)
    bookmarked_mangas = get_bookmarked_mangas(other_user)
    print(bookmarked_mangas)
    return render(request, 'manga/bookmarks.html', {"bookmarked_mangas": bookmarked_mangas})

def latest(request):
    latest_mangas = Manga.objects.filter().order_by("-posted_date")
    return render(request, 'manga/latest.html', {"latest_mangas": latest_mangas})

def categories(request):
    categories_mangas = Manga.objects.all()
    return render(request, 'manga/categories.html', {"categories_mangas": categories_mangas})

def profile(request, username):
    mangas = Manga.objects.all()

    other_user = get_object_or_404(User, username=username)
    created_mangas = get_created_mangas(other_user)
    bookmarked_mangas = get_bookmarked_mangas(other_user)

    if Follow.objects.filter(user=other_user):
        follow = Follow.objects.get(user=other_user)
    else:
        follow = Follow.objects.create(user=other_user)

    print("FOLLOWING: ", follow.following.count())
    print("FOLLOWERS: ", follow.followers.count())

    following = follow.following.all().count()
    followers = follow.followers.all().count()

    other_user_follow = {
        "following": following,
        "followers": followers, 
    }

    print("OTHER_USER ", other_user)

    other_user_follow_obj = Follow.objects.get(user=request.user)
    print(other_user_follow_obj.following.all())
    if other_user in other_user_follow_obj.following.all():
        btn_follow = False
    else:
        btn_follow = True

    print(btn_follow)
    other_user_follow["btn_follow"] = btn_follow
            
    return render(request, "manga/profile.html", {"bookmarked_mangas": bookmarked_mangas, "created_mangas": created_mangas, "username": username, "other_user_follow": other_user_follow})

def get_created_mangas(other_user):
    created_mangas = Manga.objects.filter(user=other_user)
    return created_mangas

def get_bookmarked_mangas(other_user):
    bookmarks = Bookmark.objects.filter(user=other_user)
    print(bookmarks)
    bookmarked_mangas = []
    for bookmark in bookmarks:
        bookmarked_manga = Manga.objects.get(title=bookmark.manga.title)
        bookmarked_mangas.append(bookmarked_manga)

    return bookmarked_mangas

@login_required
@csrf_exempt
def follow(request, username):
    if request.method == "POST":
        if request.user.username != username:
            data = json.loads(request.body)
            print(data["follow"])
            user = request.user
            other_user = get_object_or_404(User, username=username)

            user_follow = Follow.objects.filter(user=user)
            other_user_follow = Follow.objects.filter(user=other_user)

            #FOLLOW
            if data.get("follow") == "Follow":
                if user_follow:
                    print("User_FOLLOW:1")
                    user_follow.first().following.add(other_user)
                else:
                    print("User_FOLLOW:2")
                    user_follow = Follow.objects.create(user=user)
                    user_follow.following.add(other_user)
                    user_follow.save()

                if other_user_follow:
                    print("Other_User_FOLLOW:1")
                    other_user_follow.first().followers.add(other_user)
                else:
                    print("Other_User_FOLLOW:2")
                    other_user_follow = Follow.objects.create(user=other_user)
                    other_user_follow.followers.add(user)
                    other_user_follow.save()
                return JsonResponse({"message": "Followed successfully.", "follow": "Unfollow"})
            #UNFOLLOW
            if data.get("follow") == "Unfollow":
                if user_follow:
                    print("User_UNFOLLOW:1")
                    user_follow.first().following.remove(other_user)
                else:
                    print("User_UNFOLLOW:2")
                    user_follow = Follow.objects.create(user=user)
                    user_follow.save()

                if other_user_follow:
                    print("Other_User_UNFOLLOW:1")
                    print(other_user_follow)
                    other_user_follow.first().followers.remove(user)
                    print(other_user_follow.first().followers.all().first())
                else:
                    print("Other_User_UNFOLLOW:2")
                    other_user_follow = Follow.objects.create(user=other_user)
                    other_user_follow.save()
                return JsonResponse({"message": "Unfollowed successfully.", "follow": "Follow"})

            return JsonResponse({"message_error": "Not Follow or Unfollow"})

    return JsonResponse({"message_error": "POST request required."})

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


@login_required
@csrf_exempt
def like_comment(request, manga_id, comment_id):
    if request.method == "POST":
        comment = Comment.objects.get(id=comment_id)
        like_filter = Like.objects.filter(user=request.user, comment=comment)
        if like_filter:
            like_filter.delete()
            liked = False
            return JsonResponse({"message": "Comment unliked successfully.", "liked": liked})

        else:
            like_obj = Like(user=request.user, comment=comment).save()
            liked = True
            return JsonResponse({"message": "Comment liked successfully.", "liked": liked})
            
    return JsonResponse({"message_error": "POST request required."})

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
        return redirect("show-manga", id=id)
    else:
        return JsonResponse({"message_error": "Require POST request method"}, status=404)

def show_manga(request, id):
    manga = get_object_or_404(Manga, id=id)
    print(manga.manga_views)
    manga.manga_views = manga.manga_views + 1
    print(manga.manga_views)
    manga.save()

    comment_form = CreateComment()
    new_chapter_form = CreateNewChapter()

    manga_chapters = Chapter.objects.filter(manga=manga)
    comments = Comment.objects.filter(manga=manga).order_by("-posted_date")
    try:
        bookmark = Bookmark.objects.filter(user=request.user, manga=manga)

        if bookmark:
            bookmarked = "Bookmarked"
        else:
            bookmarked = "Bookmark"
    except:
        bookmarked = "Bookmark"

    try:
        liked_comments_id = []
        for comment in comments:
            liked_comments_id.append(Like.objects.get(user=request.user, comment=comment).comment.id)
    except:
        liked_comments_id = []


    return render(request, "manga/show_manga.html", {
        "manga": manga, 
        "manga_chapters": manga_chapters,
        "new_chapter_form": new_chapter_form,
        "comment_form": comment_form, 
        "comments": comments,
        "liked_comments_id": liked_comments_id,
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