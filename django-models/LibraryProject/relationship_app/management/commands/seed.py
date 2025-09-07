from django.core.management.base import BaseCommand
from relationship_app.models import Author, Book, Library, Librarian
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Seed the database with Authors, Books, Libraries, and Librarians'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear existing data (optional)
        Librarian.objects.all().delete()
        Library.objects.all().delete()
        Book.objects.all().delete()
        Author.objects.all().delete()

        # Create Authors
        authors = []
        for _ in range(10):
            author = Author.objects.create(name=fake.name())
            authors.append(author)
        self.stdout.write(self.style.SUCCESS('✅ Created 10 authors'))

        # Create Books
        books = []
        for _ in range(20):  # more books than authors
            book = Book.objects.create(
                title=fake.sentence(nb_words=3),
                author=random.choice(authors)
            )
            books.append(book)
        self.stdout.write(self.style.SUCCESS('✅ Created 20 books'))

        # Create Libraries
        libraries = []
        for _ in range(10):
            library = Library.objects.create(name=fake.company())
            # Add 3-7 random books to each library
            library.books.set(random.sample(books, k=random.randint(3, 7)))
            libraries.append(library)
        self.stdout.write(self.style.SUCCESS('✅ Created 10 libraries'))

        # Create Librarians
        for library in libraries:
            Librarian.objects.create(
                name=fake.name(),
                library=library
            )
        self.stdout.write(self.style.SUCCESS('✅ Created 10 librarians'))
