from rest_framework import viewsets,status
from .models import Comment,Post
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import CommentSerializer,PostSerializer
from rest_framework.permissions import IsAuthenticated


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        post = self.get_object()
        # Update the like status
        # Notify users if needed
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def save(self, request, pk=None):
        post = self.get_object()
        return Response(status=status.HTTP_200_OK)
