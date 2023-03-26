from rest_framework.viewsets import ModelViewSet
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from apps.posts.models import Post
from apps.posts.serializers import PostSerializer
from apps.posts.permissions import IsOwnerOrReadOnly


class PostsViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,IsAuthenticatedOrReadOnly)
    parser_classes = (MultiPartParser,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
