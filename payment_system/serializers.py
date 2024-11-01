from rest_framework import serializers
from .models import Payment
from django.utils import timezone

class PaymentSerializer(serializers.ModelSerializer):
    payment_date = serializers.SerializerMethodField()
    
    class Meta:
        model = Payment
        fields = ['id', 'user', 'amount', 'payment_date', 'transaction_id', 'payment_status']
        
    def get_payment_date(self, obj):
        local_time = timezone.localdate(obj.payment_date)
        return local_time.strftime("%b. %d, %Y, %I:%M %p")
     