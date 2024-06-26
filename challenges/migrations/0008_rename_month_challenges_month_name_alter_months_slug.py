# Generated by Django 4.2.2 on 2023-08-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0007_rename_month_months_month_name_alter_months_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenges',
            old_name='month',
            new_name='month_name',
        ),
        migrations.AlterField(
            model_name='months',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
