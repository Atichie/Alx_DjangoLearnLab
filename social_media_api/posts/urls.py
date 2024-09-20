from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet, FeedView, UnlikePostView
from django.urls import path

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
        path('', views.PostListView.as_view(), name='post-list'),
        path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
        path('feed/', FeedView.as_view(), name='feed'),
        path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
        path('posts/<int:pk>/like/', LikePostView.as_view(), name='unlike-post'),
]
