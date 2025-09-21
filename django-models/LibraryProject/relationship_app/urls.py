# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    # Book & Library Management
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),

    # Authentication
    path('login/', views.login_view, name='login'),  # Your custom login view
    path('login_alt/', LoginView.as_view(template_name='login.html'), name='login_alt'),  # Optional: Django's built-in LoginView
    path('register/', views.CreateUser.as_view(), name='register'),  # Class-based registration view
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path("register/", views.register, name="register"),
]
