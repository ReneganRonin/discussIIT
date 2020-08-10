from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'pages'


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    new_post = models.TextField(max_length=1000)

    def __str__(self):
        return "Author: {} | Title:{}".format(self.author, self.title)

    class Meta:
        app_label = 'pages'
