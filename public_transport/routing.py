from django.urls import path
from .consumers import LiveTrackingConsumer

websocket_urlpatterns = [
    path('ws/live_tracking/', LiveTrackingConsumer.as_asgi()),
]