from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings


BLOOD_CHOICES = (
    ('0-', 'O negative'),
    ('A-', 'A negative'),
    ('B-', 'B negative'),
    ('AB-', 'AB negative'),
    ('0+', 'O positive'),
    ('A+', 'A positive'),
    ('B+', 'B positive'),
    ('AB+', 'AB positive')
)


class Location(models.Model):

    latitude = models.FloatField(
        _('Latitude of User or Institution'),
        validators=[MinValueValidator(-90), MaxValueValidator(90)],
        default=0
    )
    longitude = models.FloatField(
        _('Longitude of User or Institution'),
        validators=[MinValueValidator(-180), MaxValueValidator(180)],
        default=0
    )


class Institution(models.Model):

    name = models.CharField(
        _('Name of Institution'),
        max_length=255
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
