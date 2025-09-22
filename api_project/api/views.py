from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer
from .models import Book
from rest_framework.permissions import BasePermission, IsAdminUser, IsAuthenticated
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


#custom permission checker class
class isAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)

class BookViewSet(viewsets.ModelViewSet):
    #custom permission checker here
    permission_classes = [IsAuthenticated,IsAdminUser,isAuthorOrReadOnly]
    queryset = Book.objects.all()
    serializer_class = BookSerializer

