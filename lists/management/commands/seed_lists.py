import random
from django.core.management.base import BaseCommand
from lists import models as list_models
from users import models as user_models
from rooms import models as room_models

class Command(BaseCommand):
    help = "This command creates lists"

    def handle(self, *args, **options):
        users = user_models.User.objects.all()
        rooms = room_models.Room.objects.all()

        for user in users:
            list_model = list_models.List.objects.create(user=user, name="Favs.")
            to_add = rooms[random.randint(0, 5) : random.randint(6, 30)]
            list_model.rooms.add(*to_add)
        self.stdout.write(self.style.SUCCESS("List created!"))