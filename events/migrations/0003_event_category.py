# Generated by Django 5.0.6 on 2024-05-29 09:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0005_category_member'),
        ('events', '0002_rename_my_event_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='boards.category'),
        ),
    ]
