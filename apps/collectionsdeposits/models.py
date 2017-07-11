from django.db import models
from apps.residents.models import Resident

class Particular(models.Model):
    name = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class Collection(models.Model):
    date = models.DateField(auto_now_add=True)
    payor = models.ForeignKey(Resident)
    particular = models.ForeignKey(Particular)
    collection = models.IntegerField()

    def __str__(self):
        return self.payor