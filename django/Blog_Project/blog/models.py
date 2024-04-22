from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.RESTRICT)
    body = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} | {self.author.username}"