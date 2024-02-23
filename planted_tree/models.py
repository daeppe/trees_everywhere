from django.db import models
from django.utils import timezone
from user.models import User
from tree.models import Tree
from account.models import Account


# Create your models here.
class PlantedTree(models.Model):
    age = models.IntegerField()
    planted_at = models.DateTimeField(timezone.now)
    location = models.CharField(max_length=50)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tree = models.ForeignKey(Tree, on_delete=models.CASCADE)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
