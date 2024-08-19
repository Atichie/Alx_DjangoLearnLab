from django.urls import path
from .views import list_books

urlpatterns = [
        path('books/', views.list_books, name='list_books'),
        path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
        path('login/', CustomLoginView.as_view(template_name='relationship_app/login.html'), name='login')
        path('logout/', CustomLogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
        path('register/',views.register, name='register'),
]

