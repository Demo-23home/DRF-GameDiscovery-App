# games/urls.py
from django.urls import path
from .views import GenreListCreateView, GameListCreateView, GameDetailView, ReviewListCreateView

urlpatterns = [
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('games/', GameListCreateView.as_view(), name='game-list-create'),
    path('games/<int:pk>/', GameDetailView.as_view(), name='game-detail'),
    path('reviews/', ReviewListCreateView.as_view(), name='review-list-create'),
]
