# Generated by Django 5.0.6 on 2024-05-25 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='my_event',
            new_name='Event',
        ),
    ]