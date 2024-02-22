from django.db import models
from django.utils import timezone


# Create your models here.
class UserProfile(models.Model):
    about = models.TextField()
    joined = models.DateTimeField(timezone.now)
