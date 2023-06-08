from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = PageNumberPagination
    pagination_class.page_size = 5
