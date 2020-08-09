from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    author = models.CharField(max_length=40, default="AnonymousUser")
    title = models.CharField(max_length=40)
    new_post = models.TextField(max_length=1000)

    class Meta:
        app_label = 'pages'
