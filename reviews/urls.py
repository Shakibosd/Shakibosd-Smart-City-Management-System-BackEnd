from django.urls import path
from .views import ReviewCreategenericsView, ReviewListAPIView

urlpatterns = [
    path('reviews/', ReviewCreategenericsView.as_view(), name='review-create'),
    path('reviews_list/<int:transport__id>/', ReviewListAPIView.as_view(), name='review-list')
]
