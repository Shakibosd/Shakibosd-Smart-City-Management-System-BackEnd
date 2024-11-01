from django.urls import path
from .views import PasswordChangeAPIView, PasswordResetRequestAPIView, RegisterAPIView, user_activate, LoginAPIView, LogoutAPIView, UserProfileListAPIView, UserProfileDetailAPIView

urlpatterns = [
    path('user_list_profile/', UserProfileListAPIView.as_view(), name='user_list_profile'),
    path('user_detail_profile/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user_detail_profile'),
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('active/<uid64>/<token>/', user_activate, name='active'),
    path('password-reset/', PasswordResetRequestAPIView.as_view(), name='password-reset-request'),
    path('reset-password/<uid64>/<token>/', PasswordChangeAPIView.as_view(), name='password-change'),
]