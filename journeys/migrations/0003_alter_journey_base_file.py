# Generated by Django 5.0.1 on 2024-02-04 05:43

import journeys.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journeys', '0002_journey_base_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journey',
            name='base_file',
            field=models.FileField(null=True, storage=journeys.models.select_storage, upload_to=''),
        ),
    ]
