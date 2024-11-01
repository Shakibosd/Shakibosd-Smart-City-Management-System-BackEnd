from django.utils import timezone
from rest_framework import serializers
from .models import EmergencyService

class EmergencyServiceSerializer(serializers.ModelSerializer):
    times_dates = serializers.SerializerMethodField()
    
    class Meta:
        model = EmergencyService
        fields = ['id', 'name', 'phone_number', 'times_dates']
        
    def get_times_dates(self, obj):
        local_time = timezone.localtime(obj.times_dates)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")  
    