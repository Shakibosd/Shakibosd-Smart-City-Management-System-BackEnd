from rest_framework import serializers
from .models import TrafficUpdate
from django.utils import timezone

class TrafficUpdateSerializer(serializers.ModelSerializer):
    last_update = serializers.SerializerMethodField()
    
    class Meta:
        model = TrafficUpdate
        fields = ['id', 'location', 'status', 'last_update']
        
    def get_last_update(self, obj):
        local_time = timezone.localtime(obj.last_update)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")  
    