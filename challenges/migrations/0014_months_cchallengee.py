# Generated by Django 4.2.2 on 2023-08-16 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0013_alter_months_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='months',
            name='cchallengee',
            field=models.CharField(max_length=100, null=True),
        ),
    ]