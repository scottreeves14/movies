from django.db import models

# Create your models here.

class Movie(models.Model):
    movieName = models.CharField(max_length=255)
    directorName = models.CharField(max_length=255)
