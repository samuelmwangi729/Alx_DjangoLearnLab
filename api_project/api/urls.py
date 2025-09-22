from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import BookList
# router = DefaultRouter()
# router.register(r'books/',BookList.as_view(),name="book_list")

# urlpatterns = [
#     path("api/",include('router.urls'))
# ]

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]