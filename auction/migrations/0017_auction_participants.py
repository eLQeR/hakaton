# Generated by Django 4.2.10 on 2024-02-11 16:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0016_alter_user_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='participants',
            field=models.ManyToManyField(default=None, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
