# Generated by Django 5.0.4 on 2024-05-11 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_alter_document_metadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='metadata',
            field=models.JSONField(default=dict),
        ),
    ]
