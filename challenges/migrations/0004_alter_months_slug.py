# Generated by Django 4.2.2 on 2023-08-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_alter_months_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='months',
            name='slug',
            field=models.SlugField(default=''),
        ),
    ]
