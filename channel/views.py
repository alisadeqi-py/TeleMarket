from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Channel, Post
from .serializers import PostSerializer


class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, channel_id):
        try:
            channel = Channel.objects.get(id = channel_id)
        except Channel.DoesNotExist:
            return Response({"error": "Channel not found"}, status = 404)

        if request.user.role != 'educator' or request.user != channel.creator:
            return Response({"error": "Permission denied"}, status = 403)

        serializer = PostSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(channel = channel, created_by = request.user)
            return Response(serializer.data, status = 201)
        return Response(serializer.errors, status = 400)

    def get(self, request, channel_id):
        try:
            channel = Channel.objects.get(id = channel_id)
        except Channel.DoesNotExist:
            return Response({"error": "Channel not found"}, status = 404)

        # Check if the user has permission to view the channel
        if  request.user.role == 'student':
            channels = channel.subscribers.all()
            if not channel.subscribers.filter(id = request.user.student_profile.id).exists():
                return Response({"error": "Permission denied"}, status = 403)

        posts = Post.objects.filter(channel = channel).order_by('-created_at')
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data, status = 200)
