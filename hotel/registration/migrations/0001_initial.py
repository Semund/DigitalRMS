# Generated by Django 4.0.5 on 2022-06-21 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_number', models.CharField(max_length=15, verbose_name='Номер паспорта')),
                ('date_of_issue', models.DateField(verbose_name='Дата выдачи')),
                ('first_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('last_name', models.CharField(max_length=50, verbose_name='Фамилия')),
                ('additional_name', models.CharField(blank=True, max_length=50, verbose_name='Дополнительное имя')),
                ('birth_date', models.DateField(verbose_name='Дата рождения')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Телефон')),
                ('email', models.CharField(blank=True, max_length=255, verbose_name='Почта')),
            ],
            options={
                'verbose_name': 'Гость',
                'verbose_name_plural': 'Гости',
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Номер',
                'verbose_name_plural': 'Номера',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateField(verbose_name='Дата заселения')),
                ('checkout_date', models.DateField(verbose_name='Дата выселения')),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.guest', verbose_name='Гость')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='registration.room', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Проживание',
                'verbose_name_plural': 'Проживания',
            },
        ),
    ]