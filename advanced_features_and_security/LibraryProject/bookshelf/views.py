from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from relationship_app.models import Book
from .forms import ExampleForm

# Create your views here.
@permission_required('bookshelf.can_edit', raise_exception=True)
def book_list(request):
    books = Book.objects.select_related("author").all()
    return render(request,"bookshelf/book_list.html",{"books":books})
def create(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Book instance
            return redirect('book_list')  # Redirect to a book list or any page you want
    else:
        form = ExampleForm()  # Empty form for GET request

    return render(request, 'bookshelf/form_example.html', {'form': form})
def delete(request):
    pass
def edit(request):
    pass