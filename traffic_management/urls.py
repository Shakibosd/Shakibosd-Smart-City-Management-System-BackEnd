from django.urls import path
from .views import TrafficStatusAPIView

urlpatterns = [
    path('traffic_status/', TrafficStatusAPIView.as_view(), name='traffic-status')
]
    