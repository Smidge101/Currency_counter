import sqlite3
from django.db import models


class Currency (models.Model):
    id = models.IntegerField(primary_key=True, unique=True,)
    name =  models.CharField(max_length=256)
    rates = models.FloatField(default=0.0)
    
    def __str__(self):
        return f"{self.name} ({self.rates})"