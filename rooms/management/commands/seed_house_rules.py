from django.core.management.base import BaseCommand
from rooms.models import HouseRule

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        house_rules = ["No smoking", "No parties/events", "Only registered guests", "Do the dishes",]
        for h in house_rules:
            HouseRule.objects.create(name=h)
        self.stdout.write(self.style.SUCCESS("House Rules created!"))