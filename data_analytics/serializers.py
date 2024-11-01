from django.utils import timezone
from rest_framework import serializers
from .models import AnalyticsData

class AnalyticsDataSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()
    
    class Meta:
        model = AnalyticsData
        fields = ['id', 'total_users', 'total_transactions', 'traffic_issues', 'date']

    def get_date(self, obj):
        local_time = timezone.localdate(obj.date)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")