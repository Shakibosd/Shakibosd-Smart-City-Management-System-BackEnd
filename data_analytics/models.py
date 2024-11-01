from django.db import models
from django.utils import timezone

class AnalyticsData(models.Model):
    total_users = models.IntegerField()
    total_transactions = models.IntegerField()
    traffic_issues = models.IntegerField()
    date = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return f"AnalyticsData on {self.date}"
