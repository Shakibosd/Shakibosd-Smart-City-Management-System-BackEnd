from django.db import models
from django.utils import timezone
from .constants import TRAFFIC_STATUS

class TrafficUpdate(models.Model):
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=TRAFFIC_STATUS)
    last_update = timezone.localtime(timezone.now())