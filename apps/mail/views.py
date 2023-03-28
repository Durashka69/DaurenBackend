from rest_framework.generics import CreateAPIView

from rest_framework.permissions import IsAuthenticated

from .models import Mail
from .serializers import MailSerializer


class MailView(CreateAPIView):
    queryset = Mail.objects.all()
    serializer_class = MailSerializer
    permission_classes = [IsAuthenticated]
