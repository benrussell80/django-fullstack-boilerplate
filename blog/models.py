from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from autoslug.fields import AutoSlugField

# Create your models here.
User = get_user_model()

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    banner = models.ImageField(upload_to='%Y-%m-%d', null=True, blank=True)
    body = models.TextField(max_length=5000)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField()
    likes = models.ManyToManyField(User, related_name='liked_posts')  # post.likes.add(<user::pk>)
    slug = AutoSlugField(populate_from='title')

    def __str__(self):
        return self.title

    @property
    def published(self) -> bool:
        if self.published_at:
            if self.published_at <= timezone.now():
                return True
            else:
                return False
        return False

    @property
    def banner_url(self) -> str:
        try:
            return self.banner.url
        except ValueError:
            return ''

    @property
    def number_of_likes(self) -> int:
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(max_length=2000)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_comments')

    def __str__(self):
        return self.body[:20] + '...'

    @property
    def number_of_likes(self) -> int:
        return self.likes.count()
