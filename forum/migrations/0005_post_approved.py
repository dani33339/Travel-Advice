# Generated by Django 3.2.9 on 2021-12-16 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0004_remove_post_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
