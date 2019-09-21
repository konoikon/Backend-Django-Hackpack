from django.db import models


# Create your models here.
class Artist(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    age = models.IntegerField()
    genre = models.CharField(max_length=300)
    artwork = models.CharField(max_length=300)
