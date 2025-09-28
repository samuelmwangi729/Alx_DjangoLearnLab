from django_filters import rest_framework as filters
from .models import Book

class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'title': ['icontains'],           # case-insensitive partial match
            'author': ['icontains'],
            'publication_year': ['exact', 'gte', 'lte'],
        }
