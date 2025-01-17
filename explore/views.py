from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import Story, ExplorePost
from .serializers import StorySerializer, PostSerializer


class ExploreView(APIView):
    def get(self, request, *args, **kwargs):
        # Fetch active stories
        active_stories = Story.objects.filter(is_active=True).order_by('-created_at')
        story_serializer = StorySerializer(active_stories, many=True)

        # Fetch paginated posts
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Number of posts per page
        paginated_posts = paginator.paginate_queryset(
            queryset=ExplorePost.objects.all().order_by('-created_at'),  # Fetch posts with pagination
            request=request,
            view=self,
        )
        post_serializer = PostSerializer(paginated_posts, many=True)

        # Combine data
        return paginator.get_paginated_response({
            'stories': story_serializer.data,
            'posts': post_serializer.data,
        })