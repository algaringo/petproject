# Generated by Django 4.0.6 on 2022-08-01 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carmechanic', '0028_forgotpassword_oldpassword_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanicrating',
            name='mechanics',
            field=models.TextField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='userpassword',
            name='newpassword',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
