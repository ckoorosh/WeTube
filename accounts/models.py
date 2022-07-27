from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    strike = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    def make_admin(self):
        self.is_admin = True
        self.save()

    def set_strike(self, strike_status):
        self.strike = strike_status
        self.save()

    def verify(self):
        self.is_verified = True
        self.save()
