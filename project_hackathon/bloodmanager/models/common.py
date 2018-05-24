from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

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

    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.IntegerField(null=True)

    def __str__(self):
        return u'%s, %s' % (
            self.address,
            self.city
        )


class Institution(models.Model):

    name = models.CharField(
        _('Name of Institution'),
        max_length=255
    )
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self):
        return u'%s' % (
            self.name,
        )
