# Generated by Django 4.2.2 on 2023-08-15 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0002_months_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='months',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]