from django.urls import path
from . import views

urlpatterns = [
        path('login/', views.auth_views.LoginView.as_view(), name='login'),
        path('logout/', views.auth_views.LogoutView.as_view(), name='logout'),
        path('register/', views.register, name='register'),
        path('profile/', views.profile, name='profile'),
        path('edit_profile/', views.edit_profile, name='edit_profile'),
]
