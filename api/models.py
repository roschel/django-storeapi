from enum import unique
from django.db import models

# Create your models here.


class Location(models.Model):
    localtionName = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.localtionName


class Item(models.Model):
    itemName = models.CharField(max_length=100)
    date_added = models.DateField(auto_now_add=True)
    itemLocation = models.ForeignKey(Location, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.itemName
