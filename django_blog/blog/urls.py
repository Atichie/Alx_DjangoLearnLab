from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import add_comment, CommentUpdateView, CommentDeleteView
urlpatterns = [
        path('login/', views.auth_views.LoginView.as_view(), name='login'),
        path('logout/', views.auth_views.LogoutView.as_view(), name='logout'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),
        path('', PostListView.as_view(), name='post-list'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
        path('post/new/', PostCreateView.as_view(), name='post-create'),
        path("post/<int:pk>/update/", PostUpdateView.as_view(), name='post-update'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
        path('post/<int:post_id>/comment/new/', add_comment, name='comment-add'),
        path('comment/<int:pk>/edit/', CommentUpdateView.as_view(), name='comment-edit'),
        path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
        path("comment/<int:pk>/update/"),
        path("post/<int:pk>/comments/new/"),
        path('tags/<str:tag_name>/', views.post_by_tag, name='post_by_tag'),
        path('search/', views.search_posts, name='Search'),
]
