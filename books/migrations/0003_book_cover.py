# Generated by Django 3.1.14 on 2021-12-25 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.ImageField(default=True, upload_to='covers/'),
        ),
    ]
