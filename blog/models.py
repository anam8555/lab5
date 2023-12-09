from django.db import models
from django.contrib.auth.models import User


class PostManager(models.Manager):
    def public_posts(self):
        return self.filter(is_public=True)


class Post(models.Model):
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=False)

    objects = PostManager()

    def __str__(self):
        return self.message
