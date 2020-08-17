from django.forms import ModelForm, Textarea
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body',)
        widgets = {
            'body': Textarea(attrs={'cols': 80,
                                    'rows': 35,
                                    'style': "resize: none",
                                    'placeholder': "Type your post here..."})
        }
