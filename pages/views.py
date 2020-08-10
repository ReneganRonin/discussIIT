from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from .forms import PostForm
from .models import Author, Post


# Create your views here.

class HomeView(View):

    @staticmethod
    def get(request):
        context = {
            'title': "Home — discussIIT",
            'content': "Some content"
        }
        return render(request, 'home.html', context=context)


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
            author = Author(name=request.user)
            author.save()
            form = author.post_set.create(title=request.POST.get('title'), new_post=request.POST.get('new_post'))
            form.save()
            return redirect('/')
