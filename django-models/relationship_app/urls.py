from django.urls import path
from .views import list_books

urlpatterns = [
        path('books/', views.list_books, name='list_books'),
        path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]


from django.urls import path
from .views import CustomLoginView, CustomLogoutView, register

urlpatterns = [
        path('login/', CustomLoginView.as_View(), name='login')
        path('logout/', CustomLogoutView.as_view(), name='logout'),
        path('register/', register, name='register'),
]

