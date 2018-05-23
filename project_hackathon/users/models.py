from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from project_hackathon.bloodmanager.models.common import BLOOD_CHOICES, Location, Institution
import datetime

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female')
)


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_('Name of User'), blank=True, max_length=255)
    email = models.EmailField(_('Email of User'), max_length=255)
    # for international telephone numbers
    telephone_number = models.CharField(
        _('Telephone number of User'),
        max_length=20
    )
    date_of_birth = models.DateField(
        _('Age of User'),
        default=datetime.date.today
    )
    gender = models.CharField(
        max_length=20,
        choices=GENDER_CHOICES,
        default=""
    )
    comment = models.CharField(
        _('Additional information such as gift-giving questionnaires blood'),
        max_length=500,
        null=True
    )
    bloodtype = models.CharField(
        max_length=50,
        choices=BLOOD_CHOICES,
        default=""
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.CASCADE
    )
    institution = models.ManyToManyField(
        Institution
    )

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('users:detail', kwargs={'username': self.username})
