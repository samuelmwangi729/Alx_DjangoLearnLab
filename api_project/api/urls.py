from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList,BookViewSet
router = DefaultRouter()
router.register(r'books_all',BookViewSet)

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),
    path('',include(router.urls)),
    path('api-token/', obtain_auth_token, name='api_token_auth'),
]
