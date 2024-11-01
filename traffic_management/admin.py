from django.contrib import admin
from .models import TrafficUpdate

class TrafficUpdateAdmin(admin.ModelAdmin):
    list_display = ['id', 'location', 'status', 'last_update']

admin.site.register(TrafficUpdate,TrafficUpdateAdmin)