# Generated by Django 4.0.6 on 2022-07-30 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carmechanic', '0009_booked_delete_booking'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booked',
            new_name='BookedMechanic',
        ),
    ]
