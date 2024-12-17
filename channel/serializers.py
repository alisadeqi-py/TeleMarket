from rest_framework import serializers
from .models import Post, Channel

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'channel', 'content', 'media_file', 'scheduled_at', 'created_at']


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = ['id', 'name', 'description', 'creator', 'is_private', 'price', 'image', 'created_at']