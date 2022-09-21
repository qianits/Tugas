from django.db import models

# Create your models here.

class MyWatchList(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField()
    rating = models.TextField()
    release_date = models.TextField()
    review = models.TextField()