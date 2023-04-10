# Generated by Django 4.1.5 on 2023-02-10 01:13

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0012_alter_ride_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='sharers',
        ),
        migrations.AddField(
            model_name='ride',
            name='sharers_party_size',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), null=True, size=None),
        ),
        migrations.AddField(
            model_name='ride',
            name='sharers_username',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
    ]