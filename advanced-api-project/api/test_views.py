# api/test_views.py

from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from api.models import Book, Author
from django.contrib.auth.models import User
from datetime import date

class BookAPITestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()

        # Create and authenticate a user
        self.user = User.objects.create_user(username='testuser', password='password123')
        self.client.force_authenticate(user=self.user)

        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')

        # Create books
        self.book1 = Book.objects.create(
            title='Book One',
            publication_year=date(2020, 1, 1),
            author=self.author1
        )
        self.book2 = Book.objects.create(
            title='Book Two',
            publication_year=date(2022, 5, 15),
            author=self.author2
        )

        self.list_url = reverse('book-list')     # Should match your DRF router names
        self.detail_url = lambda pk: reverse('book-detail', args=[pk])

    def test_get_book_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_book(self):
        response = self.client.get(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)
        self.assertEqual(response.data['author'], self.author1.id)

    def test_create_book(self):
        data = {
            'title': 'New Book',
            'publication_year': '2023-08-10',
            'author': self.author1.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(response.data['title'], 'New Book')

    def test_update_book(self):
        data = {'title': 'Updated Book Title'}
        response = self.client.patch(self.detail_url(self.book1.id), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Book Title')

    def test_delete_book(self):
        response = self.client.delete(self.detail_url(self.book1.id))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        response = self.client.get(self.list_url + f'?author={self.author1.id}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['author'], self.author1.id)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url + f'?publication_year=2020-01-01')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book One')

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url + '?search=Book Two')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Book Two')

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url + '?ordering=-publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        dates = [book['publication_year'] for book in response.data]
        self.assertEqual(dates, sorted(dates, reverse=True))

    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        # Adjust if your view is public
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # or 401
