# Generated by Django 4.2.16 on 2024-12-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0006_remove_post_media_file_post_file_alter_post_is_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='channel',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
