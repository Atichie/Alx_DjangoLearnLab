from rest_framework.routers import DefaultRouter
from .views import PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
        path('', views.PostListView.as_view(), name='post-list'),
        path('<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
]
