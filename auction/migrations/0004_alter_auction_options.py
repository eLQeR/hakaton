# Generated by Django 4.2.10 on 2024-02-10 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0003_auction_current_better'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='auction',
            options={'ordering': ['-time_of_start']},
        ),
    ]
