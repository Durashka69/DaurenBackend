from django.contrib.auth.models import User

from django.utils.decorators import method_decorator

from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from .serializers import (
    UserSerializer,
    UserLoginSerializer, 
)

from .permissions import IsOwnerOrReadOnly


@method_decorator(name='create', decorator=swagger_auto_schema(tags=["authentication"]))
class UserCreateAPIView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsOwnerOrReadOnly,)


@method_decorator(name='post', decorator=swagger_auto_schema(tags=["authentication"]))
class UserLoginAPIView(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.get_serializer(
            data=request.data, 
            context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=200)
