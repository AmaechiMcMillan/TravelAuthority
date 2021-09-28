# Generated by Django 3.2.7 on 2021-09-28 08:10

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0009_auto_20210928_0642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightbooking',
            name='leave_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 8, 10, 55, 157333)),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 8, 10, 55, 157347)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 28, 8, 10, 55, 156337)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 29, 8, 10, 55, 156355)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='zip_code',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Zippip Code'),
        ),
    ]