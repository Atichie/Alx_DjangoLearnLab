from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
        path('books/', BookListView.as_view(), name='book-list'),
        path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
        path('books/create/', BookCreateView.as_view(), name='book-detail'),
        path('books/<int:pk>update/', BookUpdateView.as_view(), name='book-update'),
        path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
        path('', include(router.urls)),
]
