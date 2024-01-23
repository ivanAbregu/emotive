from django.urls import path
from .views import MarsPhotoListAPIView

urlpatterns = [
    path('mars-photos/<str:earth_date>/', MarsPhotoListAPIView.as_view(), name='mars-photo-list'),
]
