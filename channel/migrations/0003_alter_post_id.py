# Generated by Django 4.2.16 on 2024-12-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_remove_channel_is_private_channel_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
