from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.CharField(max_length = 5)
    name = models.CharField(max_length = 25)
    age = models.IntegerField(default = 0)

    def __str__(self):
        return self.name
class Customer(models.Model):
    customer_name = models.CharField(max_length = 20)
    country = models.CharField(max_length = 20)

    def __str__(self):
        return self.customer_name