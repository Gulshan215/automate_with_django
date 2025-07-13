from django.core.management.base import BaseCommand
from dataentry.models import Student

# i want to add some data to database using the custom command
class Command(BaseCommand):
    help = 'It will insert data to the database'

    def handle(self,*args,**kwargs):
        # logic goes here
        # one data
        dataset = [
            {'roll_no':2,'name':'rohan','age':20},
            {'roll_no':5,'name':'sarthak','age':25},
            {'roll_no':4,'name':'raj','age':21}
        ]
        for data in dataset:
            roll_no = data['roll_no']
            existing_record = Student.objects.filter(roll_no = roll_no).exists()

            if not existing_record:
                Student.objects.create(roll_no = data['roll_no'] , name=data['name'], age=data['age'])
            else:
                self.stdout.write(self.style.WARNING(f'data with roll_no {roll_no} already exits'))
        self.stdout.write(self.style.SUCCESS('data inserted Successfully !'))