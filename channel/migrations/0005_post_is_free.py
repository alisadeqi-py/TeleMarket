# Generated by Django 4.2.16 on 2024-12-21 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0004_alter_channel_options_channel_subscribers_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
    ]
