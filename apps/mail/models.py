from django.db import models


class Mail(models.Model):
    email = models.EmailField(max_length=219)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Письмо'
        verbose_name_plural = 'Письма'
