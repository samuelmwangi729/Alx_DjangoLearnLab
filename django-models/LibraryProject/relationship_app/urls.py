# relationship_app/urls.py

from django.urls import path
from . import views
from .views import list_books
from django.contrib.auth.views import LoginView,LogoutView
urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('libraries/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
    path("login/",views.login_view,name="login"),
    path("register/",views.CreateUser.as_view(),name="register"),
    path("logout/",LogoutView.as_view(template_name="logout.html"),name="logout")
]
