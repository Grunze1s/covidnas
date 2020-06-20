from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

from .managers import UserManager

class User(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=20)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)