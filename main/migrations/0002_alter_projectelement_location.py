# Generated by Django 5.1.2 on 2024-11-02 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectelement',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
