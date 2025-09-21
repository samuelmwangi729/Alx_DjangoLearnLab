from django.urls import path
from . import views

urlpatterns = [
    path("all", views.book_list, name="index"),
    path("create", views.create, name="index"),
    path("edit/<int:pk>/", views.edit, name="index"),
    path("delete/<int:pk>", views.delete, name="index"),
]