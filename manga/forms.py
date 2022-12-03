from django import forms
from .models import User, Manga, Comment, Chapter
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email")

class UploadMangaForm(ModelForm):
    class Meta:
        model = Manga
        fields = ['author', 'title', 'cover', 'summary']

class CreateComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class CreateNewChapter(ModelForm):
    class Meta:
        model = Chapter
        fields = ['chapter_number', 'image']