from django.db import models
from django.utils import timezone

from user.models import User


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(timezone.now)
    active = models.BooleanField(default=True)

    user = models.ManyToManyField(User, related_name="accounts")
