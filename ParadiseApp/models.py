from django.db import models

class Roll(models.Model):
    producer = models.CharField(max_length=20)
    number = models.IntegerField()
    batch = models.IntegerField(null=True)
    size = models.CharField(max_length=20)
    coating = models.CharField(max_length=20)
    hardness = models.CharField(max_length=20)
    net = models.IntegerField()
    gross = models.IntegerField()
    remainder = models.IntegerField()
    defective = models.BooleanField(default=False)


class Plan (models.Model):
    date = models.DateField()
    roll = models.ForeignKey(Roll, on_delete=models.CASCADE)
    format = models.CharField(max_length=10)


