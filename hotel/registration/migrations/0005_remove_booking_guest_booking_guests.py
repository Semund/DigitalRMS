# Generated by Django 4.0.5 on 2022-06-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_remove_booking_guest_booking_guest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='guest',
        ),
        migrations.AddField(
            model_name='booking',
            name='guests',
            field=models.ManyToManyField(related_name='booking_guest', to='registration.guest'),
        ),
    ]
