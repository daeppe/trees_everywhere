from django.db import models


# Create your models here.
class Tree(models.Model):
    name = models.CharField(max_length=50)
    scientific_name = models.CharField(max_length=50)
