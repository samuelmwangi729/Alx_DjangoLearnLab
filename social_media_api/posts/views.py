from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from posts.models import Post, Comment
from posts.serializers import PostSerializer, CommentSerializer

# Custom Permissions
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # SAFE_METHODS = GET, HEAD, OPTIONS
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user or obj.user == request.user  # For Post or Comment


# Pagination
class DefaultPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = DefaultPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
