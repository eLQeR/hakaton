# Generated by Django 4.2.10 on 2024-02-11 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0013_alter_auction_current_bet_alter_auction_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to='auction-images-custom/'
            ),
        ),
    ]
