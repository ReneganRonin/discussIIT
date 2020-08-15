from django.shortcuts import render, redirect
from django.views import View
from users.models import CustomUser
from .forms import PostForm
from .models import Author


# Create your views here.

class PostView(View):
    @staticmethod
    def get(request):
        if request.method == 'GET':
            form = PostForm()
            form.author = request.user
            print(form)
            return render(request, 'new_post.html', {'title': "New Post — discussIIT", 'form': form})

    @staticmethod
    def post(request):
        if request.method == 'POST':
            user = CustomUser.objects.get(username=request.user)
            if user.is_authenticated:
                author = Author(user=user, name=request.user)
                author.save()
                form = author.post_set.create(title=request.POST.get(
                    'title'), body=request.POST.get('body'))
                form.save()
                return redirect('/')

            # this one is the same path but only with login and signup content
            return redirect('/')
