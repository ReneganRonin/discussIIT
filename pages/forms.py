from django.forms import ModelForm, Textarea
from .models import Post
from django.contrib.auth.models import User


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'new_post',)
        widgets = {
            'new_post': Textarea(attrs={'cols': 80, 'rows': 20})
        }
