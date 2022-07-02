from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Manga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.TextField()
    manga_title = models.TextField()
    summary = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga_title}"

class Chapter(models.Model):
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    chapter_title = models.TextField(null="true", blank="true")
    chapter_number = models.IntegerField(default=0)
    image = models.ImageField()

    def __str__(self):
        return f"{self.manga.manga_title} chapter {self.chapter_number}"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manga.manga_title} bookmarked by {self.user.username}"

class Avaliation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    avaliation = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.manga.manga_title} - {self.user.username}:{self.avaliation}"


    
