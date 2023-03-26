from django.db import models
from django.core.validators import RegexValidator

from apps.users.models import User

from uuid import uuid4


def generate_filename(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{str(uuid4())}.{ext}"
    return f"{filename}"


class Post(models.Model):
    user = models.ForeignKey(
        User, 
        verbose_name='пользователь', 
        on_delete=models.CASCADE, 
        related_name='posts'
    )
    is_businessman = models.BooleanField(default=True, verbose_name='является ли бизнесменом')
    title = models.CharField(max_length=255)
    description = models.TextField(verbose_name='Пост')
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Phone number",
        help_text="Enter phone number in international format",
        unique=True,
        db_index=True,
        validators=[
            RegexValidator(
                regex=r"^\+(?:[0-9] ?){6,14}[0-9]$",
                message='Phone number must be entered in the format: "+999999999". Up to 15 digits allowed.',
            )
        ],
    )
    image = models.ImageField(upload_to=generate_filename)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} -- {self.title}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
