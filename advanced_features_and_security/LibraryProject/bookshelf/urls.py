from django.urls import path
from . import views

urlpatterns = [
    path("all", views.book_list, name="book_list"),
    path("create", views.create, name="books.create"),
    path("edit/<int:pk>/", views.edit, name="book.edit"),
    path("delete/<int:pk>", views.delete, name="book.delete"),
]