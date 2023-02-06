# Generated by Django 4.1.5 on 2023-02-06 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ride', '0002_account_vehicle_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('CM', 'compact'), ('SU', 'suv'), ('LX', 'luxury'), ('MV', 'minivan')], default='CM', max_length=2),
        ),
    ]
