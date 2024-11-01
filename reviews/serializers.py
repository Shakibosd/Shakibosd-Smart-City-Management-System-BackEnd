from rest_framework import serializers
from .models import Review
from django.utils import timezone

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    transport = serializers.StringRelatedField()
    created_at = serializers.SerializerMethodField()
    
    class Meta:
        model = Review
        fields = ['id', 'user', 'transport', 'comment', 'rating', 'created_at']
        
    def get_created_at(self, obj):
        local_time = timezone.localtime(obj.created_at)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")      