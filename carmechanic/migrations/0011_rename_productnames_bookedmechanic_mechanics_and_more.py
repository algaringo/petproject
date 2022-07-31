# Generated by Django 4.0.6 on 2022-07-30 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmechanic', '0010_rename_booked_bookedmechanic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookedmechanic',
            old_name='productnames',
            new_name='mechanics',
        ),
        migrations.RenameField(
            model_name='bookedmechanic',
            old_name='prices',
            new_name='rates',
        ),
        migrations.AddField(
            model_name='bookedmechanic',
            name='locations',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]