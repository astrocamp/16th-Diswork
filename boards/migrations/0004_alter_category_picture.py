# Generated by Django 5.0.6 on 2024-05-24 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boards', '0003_category_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
