from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length = 30, blank = True)
    age = models.IntegerField(null = True, blank = True)

# Create your models here.
