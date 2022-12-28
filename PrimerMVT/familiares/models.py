from django.db import models


class Familiares(models.Model):
    nombre = models.CharField(max_length = 30)
    estatura = models.FloatField()
    casado = models.BooleanField()