# Generated by Django 4.0.6 on 2022-07-30 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmechanic', '0011_rename_productnames_bookedmechanic_mechanics_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mechanics', models.CharField(max_length=20)),
                ('buyer', models.CharField(blank=True, max_length=50, null=True)),
                ('rates', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('listingid', models.IntegerField()),
            ],
        ),
    ]
