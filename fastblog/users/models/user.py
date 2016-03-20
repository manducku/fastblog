from django.db import models 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phonenumber = models.CharField(
            max_length=20,
            blank=True,
            null=True,
            )

    class Meta:
        verbose_name = "member info"
        verbose_name_plural = verbose_name



