from django.contrib import admin
from .models import IncidentReport

class IncidentReportAdmin(admin.ModelAdmin):
    list_display = ['id', 'incident_type', 'description', 'reported_by', 'report_date', 'location']

admin.site.register(IncidentReport, IncidentReportAdmin)