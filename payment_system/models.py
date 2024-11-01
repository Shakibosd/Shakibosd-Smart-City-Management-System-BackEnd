from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from .constants import PAYMENT_STATUS

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    payment_date = timezone.localtime(timezone.now())
    transaction_id = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100, choices=PAYMENT_STATUS)
    
    def __str__(self):
        return f'{self.user.username} - {self.transaction_id}'