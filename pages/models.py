from django.db import models
from django.conf import settings


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=40)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return "Author: {} | Title:{}".format(self.author, self.title)

    class Meta:
        app_label = 'pages'
