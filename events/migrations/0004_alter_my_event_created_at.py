# Generated by Django 5.0.4 on 2024-05-16 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_my_event_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_event',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]