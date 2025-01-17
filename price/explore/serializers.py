from rest_framework import serializers
from .models import Story, ExplorePost


class StorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Story
        fields = ['id', 'user', 'image', 'caption', 'created_at']

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExplorePost
        fields = ['id', 'user', 'file', 'caption', 'created_at', 'total_likes']
