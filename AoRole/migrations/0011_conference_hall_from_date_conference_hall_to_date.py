# Generated by Django 4.0.6 on 2022-07-14 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AoRole', '0010_conference_hall_from_date_conference_hall_to_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference_hall',
            name='from_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='conference_hall',
            name='to_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
