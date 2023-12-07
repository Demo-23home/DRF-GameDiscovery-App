# yourapp/management/commands/add_genres.py

from django.core.management.base import BaseCommand
from games.models import Genre

class Command(BaseCommand):
    help = 'Add genres to the database'

    def handle(self, *args, **kwargs):
        self.add_genres()

    def add_genres(self):
        # List of genres to add
        genres_to_add = ['Action', 'Adventure', 'Strategy', 'Simulation', 'Racing']

        for genre_name in genres_to_add:
            Genre.objects.create(name=genre_name)
            self.stdout.write(self.style.SUCCESS(f'Genre "{genre_name}" added successfully.'))
