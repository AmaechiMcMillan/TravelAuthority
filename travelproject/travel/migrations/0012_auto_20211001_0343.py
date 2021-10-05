# Generated by Django 3.2.7 on 2021-10-01 03:43

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0011_auto_20210928_1432'),
    ]

    operations = [
        migrations.CreateModel(
            name='TravelProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('dob', models.DateField()),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='Address')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='City')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='Zip Code')),
                ('country', models.CharField(blank=True, max_length=100, null=True, verbose_name='Country')),
                ('longitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Longitude')),
                ('latitude', models.CharField(blank=True, max_length=50, null=True, verbose_name='Latitude')),
                ('is_active', models.BooleanField(default=True)),
                ('email_verified', models.BooleanField(default=False)),
                ('has_profile', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='leave_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 1, 3, 43, 7, 319462)),
        ),
        migrations.AlterField(
            model_name='flightbooking',
            name='return_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 1, 3, 43, 7, 319473)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 1, 3, 43, 7, 318451)),
        ),
        migrations.AlterField(
            model_name='hotelbooking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 2, 3, 43, 7, 318470)),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
