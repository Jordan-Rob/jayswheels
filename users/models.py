from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    age = models.IntegerField(null=False, blank=False)
    address = models.CharField(null=False, blank=False, max_length=30)
