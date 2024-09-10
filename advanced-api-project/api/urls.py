from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView
from django.urls import path, include
from . import views
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
        path('books/',views.BookListView.as_view(), name='book-list'),
        path('books/<int:pk>/',views.BookDetailView.as_view(), name='book-detail'),
        path('books/create/', views.BookCreateView.as_view(), name='book-create'),
        path('books/<int:pk>update/', view.BookUpdateView.as_view(), name="books/update"),
        path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name="books/delete"),
]
