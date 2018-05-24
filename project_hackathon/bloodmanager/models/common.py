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

    def __str__(self):
        return u'%2.f, %2.f' % (
            self.latitude,
            self.longitude
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

class Notification(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    viewed = models.BooleanField(default=False)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT
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
