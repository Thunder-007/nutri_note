from django.db import models

# Create your models here.

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


class Food(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    calories = models.IntegerField()
    note = models.TextField()
    user = models.ForeignKey(DiveUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ReachedLimit(models.Model):
    limit = 1000
    user = models.ForeignKey(DiveUser, on_delete=models.CASCADE)
    reached = models.BooleanField(default=False)
    date = models.DateField()
    time = models.TimeField()
