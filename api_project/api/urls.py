from django.urls import path
from .views import BookList

urlpatterns = [
        path('books/', BookList.as_view(), name='book-list'),
]

from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = router.urls
