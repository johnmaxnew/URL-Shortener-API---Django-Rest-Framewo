from api.views import ShortenerCreateAPIView, ShortenerListAPIView
from django.urls import path

app_name='api'

urlpatterns = [
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('create/',ShortenerCreateAPIView.as_view(),name='create_api'),
]