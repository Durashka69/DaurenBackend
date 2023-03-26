from django.urls import path

from rest_framework.routers import SimpleRouter

from apps.users.views import (
    UserCreateAPIView,
    UserLoginAPIView,
)

router = SimpleRouter()

router.register("api/users", UserCreateAPIView, basename="api/users")


urlpatterns = [
    path("api/login/", UserLoginAPIView.as_view(), name="user_login"),
]

urlpatterns += router.urls
