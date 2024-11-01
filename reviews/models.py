from django.db import models
from django.contrib.auth.models import User
from public_transport.models import PublicTransport
from .constants import STAR_RATING_CHOICES
from django.utils import timezone

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transport = models.ForeignKey(PublicTransport, on_delete=models.CASCADE)
    rating = models.CharField(max_length=50, choices=STAR_RATING_CHOICES)
    comment = models.TextField()
    created_at = timezone.localtime(timezone.now())

    def __str__(self):
        return f'Review By {self.user} On {self.transport}'
