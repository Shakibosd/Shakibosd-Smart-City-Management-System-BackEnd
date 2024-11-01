from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'amount', 'payment_date', 'transaction_id', 'payment_status']

admin.site.register(Payment, PaymentAdmin)