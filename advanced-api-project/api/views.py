from django_filters.rest_framework import DjangoFilterBackend
from api.filters import BookFilter
# api/views.py
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from .permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics
from django_filters import rest_framework
# GET /books/ - List all books
class BookListView(generics.ListAPIView):
    """
    List all books with filtering, searching, and ordering support.

    Query Parameters:
    - Filtering: ?title=<title>&author=<author_id>&publication_year=<year>
    - Search: ?search=keyword
    - Ordering: ?ordering=title or ?ordering=-publication_year
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Filtering by fields
    filterset_fields = ['title', 'author', 'publication_year']
    filterset_class = BookFilter
    # Search on these fields
    search_fields = ['title', 'author']

    # Allow ordering by these fields
    ordering_fields = ['title', 'publication_year']

    # Default ordering
    ordering = ['title']

# GET /books/<id>/ - Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# POST /books/create/ - Create a new book
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# PUT /books/<id>/update/ - Update a book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

# DELETE /books/<id>/delete/ - Delete a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]