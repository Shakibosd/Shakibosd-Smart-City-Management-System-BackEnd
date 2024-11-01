from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display =  ['id', 'user', 'transport', 'comment', 'rating', 'created_at']
    
admin.site.register(Review, ReviewAdmin)    