# Generated by Django 4.0.6 on 2022-07-13 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AoRole', '0004_dynamicpanel'),
    ]

    operations = [
        migrations.AddField(
            model_name='dynamicpanel',
            name='name',
            field=models.CharField(default=None, max_length=15),
            preserve_default=False,
        ),
    ]
