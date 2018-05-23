from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from .common import Institution, BLOOD_CHOICES


class BloodAmount(models.Model):

    amount = models.IntegerField(_('Amount of blood'))
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)


class Donation(models.Model):
    datetime = models.DateTimeField(
        _('Date and time of Donation'),
        auto_now=True
    )
    report = models.NullBooleanField(
        _('Blood donation report'),
        default=False
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)


class BloodUnit(models.Model):
    expiration_date = models.DateTimeField(
        _('Date and time of expiration date'),
        auto_now=False
    )
    bloodtype = models.CharField(
        max_length=50,
        choices=BLOOD_CHOICES
    )
    donation = models.ForeignKey(Donation, on_delete=models.PROTECT)
