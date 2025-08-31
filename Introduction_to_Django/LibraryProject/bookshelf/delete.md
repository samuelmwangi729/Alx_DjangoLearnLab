from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete it
book.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})

# Verify deletion
Book.objects.all()
# Expected Output:
# <QuerySet []>
