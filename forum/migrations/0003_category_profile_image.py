# Generated by Django 3.2.9 on 2021-12-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_remove_author_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='profile_image',
            field=models.ImageField(blank=True, default='flags/flag-default.png', null=True, upload_to='flags/'),
        ),
    ]
