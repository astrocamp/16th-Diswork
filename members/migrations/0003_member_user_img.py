# Generated by Django 5.0.6 on 2024-05-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_member_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='user_img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
