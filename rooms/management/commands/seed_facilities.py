from django.core.management.base import BaseCommand
from rooms.models import Facility

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        facilities = ["Private entrance", "Paid parking", "Elevator", "Parking", "Gym"]
        for f in facilities:
            Facility.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS("Facilities created!"))