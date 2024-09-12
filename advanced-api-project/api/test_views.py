from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from api.models import status
from api.models import Book, Author
from api.serializers import Book, Author
from api.serializers import BookSerializer
from django.contrib.auth.models import User

class BookAPITests(APITestCase):
    def setup(self):
        self.client = APIClient()
        self.user = user.objects.create_user(username='testuser', password='password')
        self.author = Author.objects.create(name='John Doe')
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)
        self.client.login(username='testuser', password='password')


    def test_create_book(self):
        url = reverse('book-create')
        data = {
                'title': 'New Book',
                'publication_year': 2021,
                'author': self.author.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_get_book(self):
        url reverse('book-detail', args=[self.book.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Book')

    def test_update_book(self):
        url = reverse('book-update', args=[self.book.id])
        data = {'title': 'updated Book'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-delete', args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_N0_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = f"{reverse('book-list')}?title=Test"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        url = f"reverse('book-list')}?search=Test"
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_permission_denied(self):
        self.client.logout()
        url = reverse('book-create')
        response = self.client.post(url, {'title': 'Forbidden Book'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
