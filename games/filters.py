# games/filters.py
import django_filters
from .models import Game

class GameFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = {
            'genre__name': ['exact'],
            'platform': ['iexact'],  # Use 'iexact' for case-insensitive filtering
            'title': ['icontains'],
        }
