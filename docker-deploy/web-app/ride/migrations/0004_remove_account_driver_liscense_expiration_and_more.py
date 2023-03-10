# Generated by Django 4.1.5 on 2023-02-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0003_alter_account_vehicle_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='driver_liscense_expiration',
        ),
        migrations.RemoveField(
            model_name='account',
            name='driver_liscense_state',
        ),
        migrations.RemoveField(
            model_name='account',
            name='vehicle_color',
        ),
        migrations.RemoveField(
            model_name='account',
            name='vehicle_make',
        ),
        migrations.RemoveField(
            model_name='account',
            name='vehicle_model',
        ),
        migrations.RemoveField(
            model_name='account',
            name='vehicle_year',
        ),
        migrations.AlterField(
            model_name='ride',
            name='special_requirements',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
