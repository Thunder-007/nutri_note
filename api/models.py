from django.db import models

# Create your models here.
# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class DiveUser(AbstractUser):
    email = models.EmailField(unique=True)
    USER_LEVEL_CHOICES = (
        ('admin', 'Admin'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
        ('other', 'Custom type')
    )
    level = models.CharField(max_length=20, choices=USER_LEVEL_CHOICES, default='other')
