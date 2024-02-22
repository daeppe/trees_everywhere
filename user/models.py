# from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Tuple, List
from decimal import Decimal
from ..tree.models import Tree


# Create your models here.
class User(AbstractUser):
    def plant_tree(self, tree: Tree, location: Tuple[Decimal, Decimal]):
        pass

    def plant_trees(self, plants: List[Tree, Tuple[Decimal, Decimal]]):
        pass
