from django.urls import path
from .views import IsAdminStatusAPIView

urlpatterns = [
    path('admins/', IsAdminStatusAPIView.as_view(), name='admins')
]
