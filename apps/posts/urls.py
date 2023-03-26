from rest_framework.routers import SimpleRouter

from .views import PostsViewSet


router = SimpleRouter()

router.register('api/posts',PostsViewSet, basename='api/posts')


urlpatterns = []
urlpatterns += router.urls
