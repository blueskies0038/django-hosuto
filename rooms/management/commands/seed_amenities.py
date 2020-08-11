from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        amenities = ["Air conditioning", "Alarm Clock", "Balcony", "Bathroom", "Bathtub", "Bed Linen", "Boating", "Cable TV",]
        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))