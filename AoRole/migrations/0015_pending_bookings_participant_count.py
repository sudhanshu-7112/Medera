# Generated by Django 4.0.6 on 2022-07-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AoRole', '0014_pending_bookings'),
    ]

    operations = [
        migrations.AddField(
            model_name='pending_bookings',
            name='Participant_count',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
