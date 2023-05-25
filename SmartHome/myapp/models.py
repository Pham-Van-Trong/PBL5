from django.db import models

# Create your models here.


class ArduinoData(models.Model):
    name = models.CharField(max_length=100)
    value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Item(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
