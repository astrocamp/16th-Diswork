# Generated by Django 5.0.6 on 2024-05-22 19:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecomment',
            old_name='like_sender',
            new_name='like_by',
        ),
    ]
