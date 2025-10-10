from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from posts.models import Comment, Like, Post
from posts.serializers import PostSerializer, CommentSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from notifications.utils import create_notification
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
        
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_feed(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response({'detail': 'Post not found.'}, status=404)

    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({'detail': 'You have already liked this post.'}, status=400)

    if post.author != request.user:
        create_notification(
            recipient=post.author,
            actor=request.user,
            verb='liked',
            target=post
        )

    return Response({'detail': 'Post liked.'}, status=200)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    try:
        like = Like.objects.get(user=request.user, post__pk=pk)
        like.delete()
        return Response({'detail': 'Post unliked.'}, status=200)
    except Like.DoesNotExist:
        return Response({'detail': 'Like not found.'}, status=404)