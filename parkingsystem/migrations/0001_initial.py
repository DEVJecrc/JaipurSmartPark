# Generated by Django 2.0.6 on 2018-06-21 08:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ParkingLot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('rfid', models.PositiveIntegerField()),
                ('capacity_car', models.PositiveIntegerField()),
                ('capacity_motorbike', models.PositiveIntegerField()),
                ('car_space_taken', models.PositiveIntegerField()),
                ('motorbike_space_taken', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpace',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular parking space across the whole city', primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('t', 'Taken'), ('a', 'Available'), ('r', 'Reserved')], default='a', help_text='Parking space availability', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='ParkingSpaceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_start', models.DateField()),
                ('date_end', models.DateField()),
                ('time_start', models.TimeField()),
                ('time_end', models.TimeField()),
                ('duration', models.DurationField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=150)),
                ('model', models.CharField(max_length=150)),
                ('car', models.BooleanField()),
                ('motorbike', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StandaloneParkingSpace',
            fields=[
                ('parkingspace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='parkingsystem.ParkingSpace')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('price', models.PositiveIntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
            bases=('parkingsystem.parkingspace',),
        ),
        migrations.AddField(
            model_name='ticket',
            name='parking_space',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingsystem.ParkingSpace'),
        ),
        migrations.AddField(
            model_name='ticket',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkingsystem.Vehicle'),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='parking_lot',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='parkingsystem.ParkingLot'),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='taken_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='parkingspace',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='parkingsystem.ParkingSpaceType'),
        ),
        migrations.CreateModel(
            name='UserOwnedSPC',
            fields=[
                ('standaloneparkingspace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='parkingsystem.StandaloneParkingSpace')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('parkingsystem.standaloneparkingspace',),
        ),
    ]
