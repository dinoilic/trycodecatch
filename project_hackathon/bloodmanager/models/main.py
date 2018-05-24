from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from .common import Institution, BLOOD_CHOICES
from django.db.models.signals import post_save
from django.dispatch import receiver

class BloodAmount(models.Model):

    amount = models.IntegerField(_('Amount of blood'))
    institution = models.ForeignKey(Institution, on_delete=models.PROTECT)
    bloodtype = models.CharField(
        max_length=50,
        choices=BLOOD_CHOICES
    )

    def __str__(self):
        return u'%d - %s' % (
            self.amount,
            self.bloodtype
        )

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

    def __str__(self):
        return u'%s' % (
            self.datetime,
        )

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

    def __str__(self):
        return u'%s - %s' % (
            self.expiration_date,
            self.bloodtype
        )


class Event(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False)

    def __str__(self):
        return u'%s - %s' % (
            self.name,
            self.datetime
        )


class EventUser(models.Model):
    answer = models.CharField(max_length=100)
    donation = models.ForeignKey(
        Donation,
        on_delete=models.PROTECT
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )

    def __str__(self):
        return u'%s' % (
            self.answer,
        )

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
    )
    event = models.ForeignKey(
        Event, 
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return u'%s - %s' % (
            self.title,
            self.user.username
        )


@receiver(post_save, sender=Notification)
def delete_notification(sender, instance, **kwargs):
    notifications = Notification.objects.filter(
        user=instance.user
    )

    for notification in notifications:
        if notification.viewed:
            notification.delete()
