"""
Definition of models.
"""

from django.db import models

class Item(models.Model):
    title = models.CharField(max_length = 200)
    decription = models.TextField()
    amount = models.IntegerField()

