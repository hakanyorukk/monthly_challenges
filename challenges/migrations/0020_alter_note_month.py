# Generated by Django 4.2.2 on 2023-08-21 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0019_alter_months_challenge_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='month',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='challenges.months'),
        ),
    ]
