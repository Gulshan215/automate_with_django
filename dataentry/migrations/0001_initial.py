# Generated by Django 5.1.6 on 2025-07-13 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=5)),
                ('name', models.CharField(max_length=25)),
                ('age', models.IntegerField(default=0)),
            ],
        ),
    ]
