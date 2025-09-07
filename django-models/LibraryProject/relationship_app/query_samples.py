#load  the queries here 

import django 
import os


#set the environment here 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","django_models.settings")
django.setup()

from relationship_app.models import Author,Book,Librarian,Library

#query al books 
def books_by_author(author):
    author = Author.objects.get(name=author)
    return Book.objects.filter(author=author)

#list all books in a library 

def books_in_lib(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

#retrieve the librarian for the library 
def get_librarian(library_name):
    lib = Library.objects.get(name=library_name)
    return Librarian.objects.filter(library=lib)