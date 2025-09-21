from bookshelf.models import Book

# Retrieve all books
books = Book.objects.get(title="1984")
books
# Expected Output:
# <QuerySet [<Book: 1984 by George Orwell (1949)>]>
