from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, generics
from .models import Post, Comment, Notification
from .serializers import PostSerializer, CommentSerializer, ModelSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import NotificationSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'content']
    ordering_fields = ['created_at', 'title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

class LikePostView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        Like.objects.get_orcreate(user=request.user, post=post)


        if created:
            mmmm
            Notification.objects.create(
                    mmmmm
                    recipient=post.author,
                    actor=request.user,
                    verb='liked your post',
                    target=post
            )
            return Response({'message': 'PostLiked.'})
        else:
            return Response({'message': ' You have already liked this post.'}, status=400)

class UnlikePostView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, pk):
        post = Post.objects.get(pk=pk)
        like Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({'message', 'Post unliked.'})
        return Response({'message': 'You have not liked this post.'}, status=400)


