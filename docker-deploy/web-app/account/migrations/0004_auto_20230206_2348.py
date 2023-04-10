# Generated by Django 3.2.17 on 2023-02-07 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='driver_liscense',
        ),
        migrations.AddField(
            model_name='account',
            name='driver_license',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='vehicle_plate',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('CM', 'compact'), ('SU', 'suv'), ('LX', 'luxury'), ('MV', 'minivan')], default='CM', max_length=2, null=True),
        ),
    ]