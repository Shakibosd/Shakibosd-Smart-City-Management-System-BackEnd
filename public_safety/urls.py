from django.urls import path
from .views import EmergencyServiceAPIView

urlpatterns = [
    path('safety/', EmergencyServiceAPIView.as_view(), name='public-safety')
]
