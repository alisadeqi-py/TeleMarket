# Generated by Django 4.2.16 on 2025-01-15 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0002_rename_post_explorepost'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='explorepost',
            name='tags',
        ),
    ]
