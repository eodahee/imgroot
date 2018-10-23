from django.db import models

# Create your models here.
class BlockChain(models.Model) :
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.CharField(max_length=30)
    date = models.DateTimeField()
