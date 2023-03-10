
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib import auth
from django.urls import reverse


class CarType(models.TextChoices):
        COMPACT = 'CM', _('compact')
        SUV = 'SU', _('suv')
        LUXURY = 'LX', _('luxury')
        MINIVAN = 'MV', _('minivan')

class Account(models.Model):
    # link account with User
    uid = models.AutoField(primary_key=True, unique=True)
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    is_driver = models.BooleanField(default=False)

    # below are optional (driver only)
    # refer to: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
    phone = models.CharField(max_length=100, blank=True, null=True)
    vehicle_plate = models.CharField(max_length=100, blank=True, null=True)
    vehicle_type = models.CharField(max_length=2, choices=CarType.choices, default=CarType.COMPACT, blank=True, null=True)
    vehicle_seats = models.IntegerField(blank=True, null=True)
    driver_license = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.username



    