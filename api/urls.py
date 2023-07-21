from django.urls import path
from api.views import ShortenerListAPIView,ShortenerCreateApiView

app_name = 'api'

urlpatterns = [
    path('',ShortenerListAPIView.as_view(),name='all_links'),
    path('create/',ShortenerCreateApiView.as_view(),name='create_api'),
]