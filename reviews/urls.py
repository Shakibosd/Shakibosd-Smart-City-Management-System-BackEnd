from django.urls import path
from .views import ReviewCreateView, ReviewDetailView, ReviewListAPIView

urlpatterns = [
    path('reviews/', ReviewCreateView.as_view(), name='review-create'),
    path('reviews_list/<int:transport__id>/', ReviewListAPIView.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
]
