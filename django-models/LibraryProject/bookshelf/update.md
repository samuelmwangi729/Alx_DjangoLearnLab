from bookshelf.models import Book

# Get the book
book = Book.objects.get(title="1984")

# Update title
book.title = "Nineteen Eighty-Four"
book.save()

book
# Expected Output:
# <Book: Nineteen Eighty-Four by George Orwell (1949)>
