# Generated by Django 4.0.5 on 2022-06-25 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guest',
            name='passport_number',
            field=models.CharField(max_length=16, unique=True, verbose_name='Номер паспорта'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='phone',
            field=models.CharField(blank=True, max_length=15, verbose_name='Телефон'),
        ),
    ]