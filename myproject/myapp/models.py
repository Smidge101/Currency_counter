import sqlite3
from django.db import models
from . import manual


class Currency (models.Model):
    id = models.IntegerField(primary_key=True, unique=True,)
    name =  models.CharField(max_length=256)
    rates = models.FloatField(default=0.0)


def USDToWant(USD, want):
#basically get database connection 
    conn = manual.get_db_connection() 
    cursor = conn.cursor() 
   # using cursor and execute use select and user input string to get 
    #conversion rate
    #propser
    res = cursor.execute("""""")
    conversion_rate = res.fetchone()
    conn.commit() 
    conn.close()

    total = USD * conversion_rate

    return total