from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

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
]
