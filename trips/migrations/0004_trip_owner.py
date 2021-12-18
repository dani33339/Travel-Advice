# Generated by Django 3.2.9 on 2021-12-16 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_username'),
        ('trips', '0003_auto_20211208_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile'),
        ),
    ]
