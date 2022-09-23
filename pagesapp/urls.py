from django.urls import path, include
from .views import HomeView, AboutView

urlpatterns = [
    path('', HomeView, name = 'home'),
    path('about/', AboutView, name = 'about'),
]