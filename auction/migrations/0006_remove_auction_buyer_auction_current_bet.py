# Generated by Django 4.2.10 on 2024-02-10 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0005_auction_seconds_to_end'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='buyer',
        ),
        migrations.AddField(
            model_name='auction',
            name='current_bet',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
