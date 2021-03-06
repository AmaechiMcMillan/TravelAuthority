# Generated by Django 3.2.7 on 2021-09-28 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_auto_20210928_0810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightbooking',
            name='leave_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 14, 32, 26, 375137)),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 14, 32, 26, 375148)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 14, 32, 26, 374122)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 14, 32, 26, 374143)),
        ),
    ]
