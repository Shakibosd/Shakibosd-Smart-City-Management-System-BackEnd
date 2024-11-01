from django.contrib import admin
from .models import EmergencyService

class EmergencyServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'phone_number', 'times_dates']

admin.site.register(EmergencyService, EmergencyServiceAdmin)