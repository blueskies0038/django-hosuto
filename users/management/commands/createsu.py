from django.core.management.base import BaseCommand
from users.models import User


class Command(BaseCommand):

    help = "This command creates a superuser"

    def handle(self, *args, **options):
        admin = User.objects.get_or_none(username="hosuto-admin")
        if not admin:
            User.objects.create_superuser("hosuto-admin", "jennybao1004@gmail.com", "Pringles!0")
            self.stdout.write(self.style.SUCCESS(f"Superuser Created"))
        else:
            self.stdout.write(self.style.SUCCESS(f"Superuser Exists"))