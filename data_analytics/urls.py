from django.urls import path
from .views import AnalyticsDataView

urlpatterns = [
    path('analytics/', AnalyticsDataView.as_view(), name='data-analytics'),
]
