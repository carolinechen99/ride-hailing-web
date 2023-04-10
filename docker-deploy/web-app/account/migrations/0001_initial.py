# Generated by Django 4.1.5 on 2023-02-06 03:25

from django.db import migrations, models


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
                ('vehicle_plate', models.CharField(blank=True, max_length=100)),
                ('vehicle_type', models.CharField(blank=True, choices=[('CM', 'compact'), ('SU', 'suv'), ('LX', 'luxury'), ('MV', 'minivan')], default='CM', max_length=2)),
                ('vehicle_seats', models.IntegerField(blank=True, null=True)),
                ('driver_liscense', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]