from django.shortcuts import render, redirect
from django.views import View
from users.models import CustomUser
from .forms import PostForm
from .models import Post


# Create your views here.

class PostView(View):
    @staticmethod
    def get(request):
        if request.method == 'GET':
            form = PostForm()
            return render(request, 'new_post.html', {'title': "New Post — discussIIT", 'form': form})

    @staticmethod
    def post(request):
        if request.method == 'POST':
            user = CustomUser.objects.get(username=request.user)
            if user.is_authenticated:
                form = Post(author=user, title=request.POST.get('title'), body=request.POST.get('body'))
                form.save()
                return redirect('/')

            return redirect('/')  # this one is the same path but only with login and signup content


class FeedView(View):
    @staticmethod
    def get(request):
        if request.method == 'GET':
            feed = Post.objects.all()
            return render(request, 'feed.html', {'title': "Feed — discussIIT", 'feed': feed})
