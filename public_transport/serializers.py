from rest_framework import serializers
from .models import PublicTransport
from django.utils import timezone

class PublicTransportSerializer(serializers.ModelSerializer):
    launched_officially_dateTime = serializers.SerializerMethodField()
    class Meta:
        model = PublicTransport
        fields = [
            'id', 'route_name', 'bus_number', 'available_seats', 
            'next_arrival_time', 'current_latitude', 'current_longitude', 
            'last_update', 'bus_img', 'schedules', 'launched_officially_dateTime'
        ]

    def get_launched_officially_dateTime(self, obj):
        local_time = timezone.localtime(obj.launched_officially_dateTime)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")
