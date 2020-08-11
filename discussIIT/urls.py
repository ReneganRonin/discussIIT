"""discussIIT URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic.base import TemplateView
from django.views.generic import RedirectView
from pages.views import PostView, FeedView

urlpatterns = [
    # from users
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
    # some JSON emoji list
    re_path(r'^emoji/', include('emoji.urls')),
    # from pages
    path('feed/', RedirectView.as_view(url='feed')),
    path('feed', FeedView.as_view(), name='feed'),
    path('post', PostView.as_view(), name='post'),
    path('post/post', RedirectView.as_view(url='post')),
    path('admin/', admin.site.urls),
]
