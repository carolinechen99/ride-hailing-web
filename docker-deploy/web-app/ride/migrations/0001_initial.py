# Generated by Django 4.1.5 on 2023-02-05 23:39

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('is_driver', models.BooleanField()),
                ('vehicle_color', models.CharField(blank=True, max_length=100)),
                ('vehicle_plate', models.CharField(blank=True, max_length=100)),
                ('vehicle_make', models.CharField(blank=True, max_length=100)),
                ('vehicle_model', models.CharField(blank=True, max_length=100)),
                ('vehicle_year', models.IntegerField(blank=True, null=True)),
                ('vehicle_seats', models.IntegerField(blank=True, null=True)),
                ('driver_liscense', models.CharField(blank=True, max_length=100)),
                ('driver_liscense_expiration', models.DateField(blank=True, null=True)),
                ('driver_liscense_state', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('owner_party_size', models.IntegerField()),
                ('sharers', django.contrib.postgres.fields.ArrayField(base_field=models.JSONField(), null=True, size=None)),
                ('required_arrival_time', models.DateTimeField()),
                ('pickup_location', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('OP', 'open'), ('CF', 'confirmed'), ('CP', 'completed'), ('CL', 'cancelled')], default='OP', max_length=2)),
                ('allow_sharing', models.BooleanField()),
                ('special_requirements', models.CharField(max_length=100)),
                ('driver_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='driver', to='ride.account')),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='owner', to='ride.account')),
            ],
        ),
    ]
