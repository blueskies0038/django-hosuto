import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):
    help = "This command creates reviews"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()
        seeder.add_entity(review_models.Review, 10,
                          {
                              "accuracy": lambda x: random.randint(1,6),
                              "communication": lambda x: random.randint(1,6),
                              "cleanliness": lambda x: random.randint(1,6),
                              "value": lambda x: random.randint(1,6),
                              "room": lambda x: random.choice(rooms),
                               "user": lambda x: random.choice(users)
                          },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS("Review created!"))