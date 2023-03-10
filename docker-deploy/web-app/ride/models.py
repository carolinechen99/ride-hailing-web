from django.db import models
# from postgres_composite_types import CompositeType
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from account.models import Account
from django.contrib.auth.models import User

class Status(models.TextChoices):
        OPEN = 'OP', _('open')
        CONFIRMED = 'CF', _('confirmed')
        COMPLETED = 'CP', _('completed')
        CANCELLED = 'CL', _('cancelled')


class CarType(models.TextChoices):
        COMPACT = 'CM', _('compact')
        SUV = 'SU', _('suv')
        LUXURY = 'LX', _('luxury')
        MINIVAN = 'MV', _('minivan')


# Create your models here.
class Ride(models.Model):
    rid = models.AutoField(primary_key=True)
    driver = models.ForeignKey(User, related_name='driver', on_delete=models.DO_NOTHING, null=True)
    owner = models.ForeignKey(User,related_name='owner', on_delete=models.DO_NOTHING, null=True)
    owner_party_size = models.IntegerField()
    sharers_username = ArrayField(models.CharField(max_length=100), null=True) # changed to Array of usernames
    sharers_party_size = ArrayField(models.IntegerField(), null=True) # corresponds to sharers_username
    required_arrival_time = models.DateTimeField()
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField( max_length=2, choices=Status.choices, default=Status.OPEN)
    allow_sharing = models.BooleanField()
    special_requirements = models.CharField(max_length=100, blank=True)
    vehicle_type = models.CharField(max_length=2, choices=CarType.choices, null=True)#######DEBUG: change to default=CarType.COMPACT to test

    def __str__(self):
        return self.rid

# class Account(models.Model):
#     uid = models.AutoField(primary_key=True)
#     username = models.CharField(max_length=100)
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     is_driver = models.BooleanField(default=False)

#     # below are optional (driver only)
#     # refer to: https://stackoverflow.com/questions/8609192/what-is-the-difference-between-null-true-and-blank-true-in-django
#     phone = models.CharField(max_length=100, blank=True)
#     vehicle_plate = models.CharField(max_length=100, blank=True)
#     vehicle_type = models.CharField(max_length=2, choices=CarType.choices, default=CarType.COMPACT, blank=True)
#     vehicle_seats = models.IntegerField(blank=True, null=True)
#     driver_liscense = models.CharField(max_length=100, blank=True)


