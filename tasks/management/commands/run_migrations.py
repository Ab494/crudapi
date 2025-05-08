from django.core.management.base import BaseCommand
from django.core.management import call_command
class Command(BaseCommand):
    help = "Run migrations automatically"
    def handle(self, *args, **options):
        self.stdout.write("Running migrations...")
        call_command = ("migrate")
        self.stdout.write("Migrations completed successfully.")
