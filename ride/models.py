from django.db import models
# from postgres_composite_types import CompositeType
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# class Party(CompositeType):
#     """A party with size and leader's id."""
#     party_size = models.IntegerField()
#     leader_id = models.IntegerField()
    
#     class Meta:
#         db_type = 'party'  # Required

class Status(models.TextChoices):
        OPEN = 'OP', _('open')
        CONFIRMED = 'CF', _('confirmed')
        COMPLETED = 'CP', _('completed')
        CANCELLED = 'CL', _('cancelled')


# Create your models here.
class Ride(models.Model):
    rid = models.AutoField(primary_key=True)
    driver_id = models.ForeignKey('Account', related_name='driver', on_delete=models.DO_NOTHING, null=True)
    owner_id = models.ForeignKey('Account', related_name='owner', on_delete=models.DO_NOTHING, null=True)
    owner_party_size = models.IntegerField()
    sharers = ArrayField(models.JSONField(), null=True)
    required_arrival_time = models.DateTimeField()
    pickup_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    status = models.CharField( max_length=2, choices=Status.choices, default=Status.OPEN)
    allow_sharing = models.BooleanField()
    special_requirements = models.CharField(max_length=100)

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

