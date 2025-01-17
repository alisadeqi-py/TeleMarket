# Generated by Django 4.2.16 on 2025-01-15 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0003_remove_explorepost_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='market',
            field=models.CharField(choices=[('Forex', 'Forex'), ('Crypto', 'Crypto'), ('TSE', 'Tehran Stock Exchange')], default=1, max_length=20),
            preserve_default=False,
        ),
    ]
