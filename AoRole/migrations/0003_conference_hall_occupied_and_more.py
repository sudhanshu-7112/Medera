# Generated by Django 4.0.6 on 2022-07-12 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AoRole', '0002_alter_conference_hall_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference_hall',
            name='occupied',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='conference_images',
            name='Hall',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hall', to='AoRole.conference_hall'),
        ),
    ]
