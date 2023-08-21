# Generated by Django 4.2.2 on 2023-08-21 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0018_alter_months_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='months',
            name='challenge',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='months', to='challenges.challenges'),
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('text', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now=True)),
                ('month', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='challenges.months')),
            ],
        ),
    ]
