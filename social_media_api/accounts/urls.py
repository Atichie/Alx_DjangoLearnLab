from django.urls import path, include
from .views import RegisterView, CustomObtainAuthToken

urlpatterns = [
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', CustomObtainAuthToken.as_view(), name='login'),
        path('api/accounts/', include('accounts.urls')),
        path('follow/<int:user_id>', FollowUserView.as_view(), name='follow-user'),
        path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]
