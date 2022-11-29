from django.db import models

# Create your models here.
class Currencies(models.Model):
    name = models.CharField('Name', max_length=18)
    symbol = models.CharField('Symbol', max_length=18)
    price = models.CharField('Price', max_length=18)
    rank = models.CharField('Rank', max_length=18)
    volume = models.CharField('Volume', max_length=18)