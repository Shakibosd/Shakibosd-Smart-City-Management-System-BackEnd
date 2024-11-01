from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    GENDER_CHOICE = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Custom', 'Custom'),
    ]
    RELIGION_CHOICES = [
        ('Muslim', 'Muslim'),
        ('Hindu', 'Hindu'),
        ('Buddhist', 'Buddhist'),
        ('Christian', 'Christian'),
        ('Other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    gender = models.CharField(max_length=20, choices=GENDER_CHOICE, default='Male')
    religion = models.CharField(max_length=20, choices=RELIGION_CHOICES, default='Muslim')
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_img = models.CharField(max_length=500, default='')

    def __str__(self):
        return self.user.username