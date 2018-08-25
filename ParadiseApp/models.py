from django.db import models

class Roll(models.Model):

    producer = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    coating = models.CharField(max_length=20)
    hardness = models.CharField(max_length=20)
    net = models.IntegerField()
    gross = models.IntegerField()
    defective = models.BooleanField(default=False)

