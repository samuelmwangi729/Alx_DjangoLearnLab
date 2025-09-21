from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Book
# Create your views here.
@permission_required('app_name.can_edit', raise_exception=True)
def index(request):
    books = Book.objects.select_related("author").all()
    return render(request,"book.html",{"books":books})