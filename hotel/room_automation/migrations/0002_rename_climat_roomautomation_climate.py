# Generated by Django 4.0.5 on 2022-07-15 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_automation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roomautomation',
            old_name='climat',
            new_name='climate',
        ),
    ]
