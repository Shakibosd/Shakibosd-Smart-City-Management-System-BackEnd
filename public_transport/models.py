from django.db import models
from django.utils import timezone

class PublicTransport(models.Model):
    route_name = models.CharField(max_length=200)
    bus_number = models.CharField(max_length=30)
    available_seats = models.IntegerField()
    next_arrival_time = models.CharField(max_length=200)
    current_latitude = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)
    current_longitude = models.DecimalField(max_digits=11, decimal_places=5, null=True, blank=True)
    last_update = models.CharField(max_length=300)
    schedules = models.TextField(null=True, blank=True)
    bus_img = models.CharField(max_length=200, default='')
    launched_officially_dateTime = timezone.localtime(timezone.now())
    
    def __str__(self):
        return f"{self.route_name} ({self.bus_number})"
    
    