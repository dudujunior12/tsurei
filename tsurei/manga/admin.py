from django.contrib import admin
from .models import User, Manga, Chapter, Bookmark, Category

# Register your models here.
admin.site.register(User)
admin.site.register(Manga)
admin.site.register(Chapter)
admin.site.register(Bookmark)
admin.site.register(Category)


