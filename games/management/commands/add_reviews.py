# yourapp/management/commands/add_reviews.py

from django.core.management.base import BaseCommand
from games.models import Game, Review
from django.contrib.auth.models import User
import random
from faker import Faker

fake = Faker()

class Command(BaseCommand):
    help = 'Add reviews to the database'

    def handle(self, *args, **kwargs):
        self.add_reviews()

    def add_reviews(self):
        # Get all games from the database
        games = Game.objects.all()

        if not games.exists():
            self.stdout.write(self.style.WARNING('No games found. Please create games first.'))
            return

        # Get all users from the database
        users = User.objects.all()

        if not users.exists():
            self.stdout.write(self.style.WARNING('No users found. Please create users first.'))
            return

        for game in games:
            # Choose a random user
            user = random.choice(users)

            # Generate a random rating (between 1 and 5)
            rating = random.randint(1, 5)

            # Generate a random comment
            comment = fake.paragraph()

            Review.objects.create(
                game=game,
                user=user,
                rating=rating,
                comment=comment
            )

            self.stdout.write(self.style.SUCCESS(f'Review added for "{game.title}" by {user.username}.'))
