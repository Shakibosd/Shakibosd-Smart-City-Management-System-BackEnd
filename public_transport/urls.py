from django.urls import path
from .views import PublicTransportAPIView, UpdateLocationView, TransportListView, TransportDetailAPIView

urlpatterns = [
    path('transport/', PublicTransportAPIView.as_view(), name='transport'),
    path('transport/<int:bus_id>/', TransportDetailAPIView.as_view(), name='transport-detail'),
    path('transport_filter/', TransportListView.as_view(), name='transport-filter'),
    path('update_location/<str:bus_number>/', UpdateLocationView.as_view(), name='update-location')
]
