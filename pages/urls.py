from django.urls import path
from django.views.generic import RedirectView
from .views import HomeView, PostView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post', PostView.as_view(), name='post'),
    # Redirects
    path('post/', RedirectView.as_view(url='/post'))
]
