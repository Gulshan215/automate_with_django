from django.core.management.base import BaseCommand


# proposed Command = python manage.py greeting name
# Proposed Out = Hii {name}, Good Morning
class Command(BaseCommand):
    help = 'greeting my self'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help = "Specific user name")

    def handle(self, *args, **kwargs):
        name = kwargs['name']
        greeting = f'Hii {name}, Good Morning'
        # write the login below
        self.stdout.write(greeting)