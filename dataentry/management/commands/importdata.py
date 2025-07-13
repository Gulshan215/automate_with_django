from django.core.management.base import BaseCommand, CommandError
# from dataentry.models import Student
from django.apps import apps
import csv
# Proposted Command - python manage.py importdata filepath.csv model_name
class Command(BaseCommand):

    help = 'Import data from csv file'

    def add_arguments(self, parser):
        # parser.add_argument help you to add one or more agrument. when we call the manage.py you can pass the argument that time.
        parser.add_argument('file_path', type=str, help = 'Path to the csv file')
        parser.add_argument('model_name', type=str, help = 'Name of the Model')

    def handle(self,*args,**kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()


        #search for the model across all the installed app
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model in found
            except LookupError:
                continue # model not found in this app , then continue searching in next app
            
        if not model:
            raise CommandError(f' Model "{model_name}" not found in any app ')

        with open(file_path , 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                existing_record = row['roll_no']
                if not existing_record:
                    Student.objects.create(**row)
                else:
                    self.stdout.write(self.style.WARNING('data imported for csv already exits !'))

        self.stdout.write(self.style.SUCCESS('data imported for csv Successfully !'))
