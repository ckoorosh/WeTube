from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    strike = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)



