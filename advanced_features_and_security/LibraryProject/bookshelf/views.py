from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Book
# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request,"book.html",{"books":books})
def create(request):
    pass
def delete(request):
    pass
def edit(request):
    pass