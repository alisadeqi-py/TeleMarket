from django.urls import path
from .views import CreatePostView

urlpatterns = [
    path('<str:channel_id>/posts/', CreatePostView.as_view(), name='channel-posts'),
]
