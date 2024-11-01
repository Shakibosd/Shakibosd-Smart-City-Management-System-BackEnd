from django.urls import path
from payment_system import views

urlpatterns = [
    path('payment/', views.payment, name='payment'),
]