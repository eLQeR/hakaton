# Generated by Django 4.2.10 on 2024-02-10 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0006_remove_auction_buyer_auction_current_bet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='seconds_to_end',
            field=models.PositiveIntegerField(default=60),
        ),
    ]
