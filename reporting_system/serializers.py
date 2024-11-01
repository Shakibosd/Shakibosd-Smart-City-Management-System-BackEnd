from rest_framework import serializers
from .models import IncidentReport
from django.utils import timezone

class IncidetReportSerializer(serializers.ModelSerializer):
    report_date = serializers.SerializerMethodField()
    
    class Meta:
        model = IncidentReport
        fields = ['id', 'incident_type', 'description', 'reported_by', 'report_date', 'location']
        
    def get_report_date(self, obj):
        local_time = timezone.localtime(obj.report_date)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")    