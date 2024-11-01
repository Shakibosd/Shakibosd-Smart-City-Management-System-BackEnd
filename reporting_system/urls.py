from django.urls import path
from .views import IncidentReportAPIView

urlpatterns = [
    path('reports/', IncidentReportAPIView.as_view(), name='reports')
]
