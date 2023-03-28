from django.urls import path

from .views import MailView


urlpatterns = (path('api/mails/', MailView.as_view(), name="mails"),)
