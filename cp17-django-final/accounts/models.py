from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField("Возраст", null=True, blank=True)
    bio = models.CharField("О себе", max_length=200, blank=True)

    def __str__(self):
        return self.get_full_name() or self.username
