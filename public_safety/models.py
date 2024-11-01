from django.db import models
from django.utils import timezone

class EmergencyService(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    times_dates = timezone.localtime(timezone.now())