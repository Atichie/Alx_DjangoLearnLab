from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Retrieve a list of all books.
    This view is open to both authenticated and unauthenticated users
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classers = [permissions.AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterest_fields = ['publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a specific book by it ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permission.AllowAny]

class BookCreateView(generics.CreateAPIView):
    """
    Add a new book. Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permission.IsAunthenticated]

    def perform_create(self, serializer):
        serializer.save()


class BookUpdateView(generics.UpdateAPIView):
    """
    Modifies an existing book. Restricted to aunthenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()

class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


