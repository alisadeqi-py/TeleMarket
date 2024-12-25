from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from .models import Channel, Post
from .serializers import PostSerializer


class ChanelDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch all channels with their last post (if any)
        channels = Channel.objects.all()
        channels_data = []

        for channel in channels:
            # Get the most recent post for the channel
            last_post = Post.objects.filter(channel=channel).order_by('-created_at').first()
            last_post_data = PostSerializer(last_post).data if last_post else None

            channel_data = {
                "id": channel.id,
                "name": channel.name,
                "description": channel.description,
                "is_free": channel.is_free,
                "price": channel.price,
                "image": channel.image.url if channel.image else None,
                "created_at": channel.created_at,
                "new_message_timestamp": channel.new_message_timestamp,
                "last_post": last_post_data
            }
            channels_data.append(channel_data)

        return Response(channels_data, status=200)


class ChannelPostsAPIView(APIView):
    def get(self, request, channel_id, *args, **kwargs):
        try:

            channel = Channel.objects.get(id=channel_id)
        except Channel.DoesNotExist:
            return Response({"error": "Channel not found"}, status=status.HTTP_404_NOT_FOUND)

        posts = Post.objects.filter(channel=channel)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)