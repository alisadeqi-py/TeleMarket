# Generated by Django 4.2.16 on 2024-12-09 18:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='channel',
            name='is_private',
        ),
        migrations.AddField(
            model_name='channel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='channel_images/'),
        ),
        migrations.AddField(
            model_name='channel',
            name='is_free',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='channel',
            name='new_message_timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='post',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='channel',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='channel',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
