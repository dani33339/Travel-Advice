# Generated by Django 3.2.9 on 2021-12-16 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='short_into',
            new_name='short_intro',
        ),
    ]
