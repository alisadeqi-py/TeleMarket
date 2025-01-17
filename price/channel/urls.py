from django.urls import path
from .views import ChanelDetailView, ChannelPostsAPIView


urlpatterns = [
    path('detail', ChanelDetailView.as_view(), name='channel-posts'),
    path('channels/<int:channel_id>/posts/', ChannelPostsAPIView.as_view(), name = 'channel-posts'),
]
