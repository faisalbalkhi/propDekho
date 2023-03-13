from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE_CHOICES = [
    (True, 'Agent'),
    (False, 'Individual'),
]
class User(AbstractUser):
    mobile_number = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    individual = models.BooleanField()
    agent = models.BooleanField()

    def __str__(self):
        return self.username
