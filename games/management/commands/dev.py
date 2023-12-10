# populate_db.py

import os
from django.core.management.base import BaseCommand
from django.utils import timezone
from games.models import GameDeveloper  # Replace 'your_app' with the actual name of your Django app

class Command(BaseCommand):
    help = 'Populate the database with 100 dummy GameDeveloper instances'

    def handle(self, *args, **options):
        # Generate 100 dummy developers with unique names
        developers_data = [
            {
                'name': f'Developer {i}',
                'founded_date': timezone.now(),
                'description': f'Description for Developer {i}',
            }
            for i in range(1, 101)
        ]

        # Populate the database with the generated data
        GameDeveloper.objects.bulk_create([GameDeveloper(**data) for data in developers_data])

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with 100 dummy GameDeveloper instances.'))
