from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.category_name}"


class Manga(models.Model):
    STATUS_CHOICES = (
        ("Dropped", "Dropped"),
        ("Releasing", "Releasing"),
        ("Completed", "Completed")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='mangas/')
    summary = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    manga_views = models.IntegerField(default=0, null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="categories")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Releasing")

    def __str__(self):
        return f"{self.title}"

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, related_name="chapters", on_delete=models.CASCADE)
    chapter_number = models.IntegerField(default=1)
    image = models.ImageField(upload_to='mangas/')
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga.title} chapter {self.chapter_number}"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manga.title} bookmarked by {self.user.username}"

    
