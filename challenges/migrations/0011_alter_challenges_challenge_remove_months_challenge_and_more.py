# Generated by Django 4.2.2 on 2023-08-16 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0010_remove_challenges_months_months_challenge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='challenges',
            name='challenge',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.RemoveField(
            model_name='months',
            name='challenge',
        ),
        migrations.AddField(
            model_name='months',
            name='challenge',
            field=models.ManyToManyField(blank=True, to='challenges.challenges'),
        ),
    ]
