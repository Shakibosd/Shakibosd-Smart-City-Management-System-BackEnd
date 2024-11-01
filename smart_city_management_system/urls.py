from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('authentication/', include('authentication.urls')),
    path('traffic_management/', include('traffic_management.urls')),
    path('public_safety/', include('public_safety.urls')),
    path('public_transport/', include('public_transport.urls')),
    path('reporting_system/', include('reporting_system.urls')),
    path('payment_system/', include('payment_system.urls')),
    path('data_analytics/', include('data_analytics.urls')),
    path('admins/', include('admins.urls')),
    path('reviews/', include('reviews.urls')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)