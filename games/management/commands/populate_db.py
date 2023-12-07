# yourapp/management/commands/populate_dummydata.py

from django.core.management.base import BaseCommand
from games.models import Genre, Platform, Game
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

class Command(BaseCommand):
    help = 'Populate the database with dummy game data'

    def handle(self, *args, **kwargs):
        self.populate_data()

    def generate_two_word_name(self):
        return fake.word() + ' ' + fake.word()

    def populate_data(self):
        genres = Genre.objects.all()
        platforms = [choice[0] for choice in Platform.choices]

        for _ in range(10):  # Adjust the number as needed
            title = self.generate_two_word_name()
            genre = random.choice(genres)
            release_date = fake.date_between(start_date='-2y', end_date='today')
            description = fake.paragraph()
            platform = random.choice(platforms)

            Game.objects.create(
                title=title,
                genre=genre,
                release_date=release_date,
                description=description,
                platform=platform
            )

        self.stdout.write(self.style.SUCCESS('Dummy data has been populated successfully.'))
