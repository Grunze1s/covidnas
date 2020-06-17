from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

from .managers import UserManager

class User(AbstractUser):
    phone_number = models.CharField(unique=True, max_length=20)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    username = None

    objects = UserManager()

    USERNAME_FIELD = 'phone_number'