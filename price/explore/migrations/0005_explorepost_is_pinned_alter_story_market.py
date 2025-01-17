# Generated by Django 4.2.16 on 2025-01-15 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0004_story_market'),
    ]

    operations = [
        migrations.AddField(
            model_name='explorepost',
            name='is_pinned',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='story',
            name='market',
            field=models.CharField(choices=[('Forex', 'Forex'), ('Crypto', 'Crypto'), ('TSE', 'Tehran Stock Exchange'), ('GOLDEN', 'GOLDEN')], max_length=20),
        ),
    ]
