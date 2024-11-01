from django.db import models
from django.utils import timezone

class IncidentReport(models.Model):
    incident_type = models.CharField(max_length=100) 
    description  = models.TextField()
    reported_by = models.CharField(max_length=300)
    location = models.CharField(max_length=100)  
    report_date  = timezone.localtime(timezone.now())
    
    def __str__(self):
        return f"{self.incident_type} reported by {self.reported_by}"