from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Delete it
book.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})

# Verify deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
