from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):
    uid = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    is_driver = models.BooleanField()
    # below are optional (driver only)
    # refer to: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
    vehicle_color = models.CharField(max_length=100, blank=True)
    vehicle_plate = models.CharField(max_length=100, blank=True)
    vehicle_make = models.CharField(max_length=100, blank=True)
    vehicle_model = models.CharField(max_length=100, blank=True)
    vehicle_year = models.IntegerField(blank=True, null=True)
    vehicle_seats = models.IntegerField(blank=True, null=True)
    driver_liscense = models.CharField(max_length=100, blank=True)
    driver_liscense_expiration = models.DateField(blank=True, null=True)
    driver_liscense_state = models.CharField(max_length=100, blank=True)
