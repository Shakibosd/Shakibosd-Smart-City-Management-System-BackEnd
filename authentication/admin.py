from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'gender', 'religion', 'phone_number', 'age', 'date_of_birth', 'profile_img']

admin.site.register(Profile, ProfileAdmin)