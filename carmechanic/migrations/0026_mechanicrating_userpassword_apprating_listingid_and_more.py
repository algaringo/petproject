# Generated by Django 4.0.6 on 2022-08-01 18:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('carmechanic', '0025_remove_apprating_buyer_remove_apprating_listingid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MechanicRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lister', models.CharField(blank=True, max_length=50, null=True)),
                ('mechanics', models.CharField(blank=True, max_length=50, null=True)),
                ('ratings', models.IntegerField(blank=True, null=True)),
                ('content', models.CharField(blank=True, max_length=30, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('listingid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='UserPassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usernames', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('password1', models.CharField(max_length=30)),
                ('newpassword', models.CharField(max_length=30)),
                ('security1', models.CharField(max_length=30)),
                ('security2', models.CharField(max_length=30)),
                ('security3', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='apprating',
            name='listingid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='apprating',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='apprating',
            name='ratings',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
