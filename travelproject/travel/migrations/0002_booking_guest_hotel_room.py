# Generated by Django 3.2.7 on 2021-09-23 07:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=20)),
                ('phone_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField(default=101)),
                ('room_type', models.CharField(default='standard', max_length=200)),
                ('rate', models.FloatField()),
                ('is_available', models.BooleanField(default=True)),
                ('no_of_beds', models.IntegerField(default=3)),
                ('hotel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='travel.hotel')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_date', models.DateTimeField(default=datetime.datetime(2021, 9, 23, 7, 14, 49, 290024))),
                ('checkout_date', models.DateTimeField(default=datetime.datetime(2021, 9, 24, 7, 14, 49, 290043))),
                ('check_out', models.BooleanField(default=False)),
                ('no_of_guests', models.IntegerField(default=1)),
                ('guest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.guest')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.hotel')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.room')),
            ],
        ),
    ]
