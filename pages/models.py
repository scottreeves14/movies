from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=255)
    year = models.IntegerField(default=0)
    score = models.DecimalField(default=0, max_digits=2, decimal_places=1)
