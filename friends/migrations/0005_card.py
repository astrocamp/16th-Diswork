# Generated by Django 5.0.6 on 2024-06-09 07:01

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0004_alter_friend_status'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('drawer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='draw', to=settings.AUTH_USER_MODEL)),
                ('drawn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drawn', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]