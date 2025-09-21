from django.shortcuts import render
from relationship_app.models import Book
# Create your views here.
def index(request):
    books = Book.objects.select_related("author").all()
    return render(request,"book.html",{"books":books})