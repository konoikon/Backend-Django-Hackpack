from django.db import models


class Artist(models.Model):
    """Defines the schema for an Artist object"""

    # the id gets created automatically by our database, we do not
    # need to specify it in a request
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)  # max_length is a required parameter of a CharField
    age = models.IntegerField()
    genre = models.CharField(max_length=300)
    artwork = models.CharField(max_length=300)
