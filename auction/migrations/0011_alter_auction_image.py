# Generated by Django 4.2.10 on 2024-02-11 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0010_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../static/media/auction-images'),
        ),
    ]
