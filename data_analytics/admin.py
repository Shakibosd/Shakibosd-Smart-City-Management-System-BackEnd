from django.contrib import admin
from .models import AnalyticsData

class AnalyticsDataAdmin(admin.ModelAdmin):
    list_display = ['id', 'total_users', 'total_transactions', 'traffic_issues', 'date']

admin.site.register(AnalyticsData, AnalyticsDataAdmin)
