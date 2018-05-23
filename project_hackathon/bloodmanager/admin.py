from django.contrib import admin
from project_hackathon.bloodmanager.models.common import Location, Institution
from project_hackathon.bloodmanager.models.main import BloodAmount, Donation, BloodUnit

admin.site.register(Location)
admin.site.register(Institution)
admin.site.register(BloodAmount)
admin.site.register(Donation)
admin.site.register(BloodUnit)
