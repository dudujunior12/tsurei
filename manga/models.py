from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    pass

class Manga(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='mangas/')
    summary = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    manga_views = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=20, default="Releasing")

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

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    comment_text = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.manga.title} - {self.user.username}:{self.comment_text}"

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name="followers", blank=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)

    def __str__(self):
        return f"{self.user}"

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, related_name="liked_comment", on_delete=models.CASCADE)

    def __str__(self):
        return f"On {self.comment.manga.title}, {self.user} liked {self.comment.comment_text}"


class Avaliation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manga = models.ForeignKey(Manga, on_delete=models.CASCADE)
    avaliation_number = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.manga.title} - {self.user.username}:{self.avaliation}"


    
