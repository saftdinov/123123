from django.test import TestCase
from django.urls import reverse
from .models import Author, Book, Genre


class CatalogPagesTests(TestCase):
    def test_home_page_returns_200(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)

    def test_book_list_returns_200(self):
        response = self.client.get(reverse("books"))
        self.assertEqual(response.status_code, 200)

    def test_author_list_returns_200(self):
        response = self.client.get(reverse("authors"))
        self.assertEqual(response.status_code, 200)
