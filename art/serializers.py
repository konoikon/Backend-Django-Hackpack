from .models import Artist
from rest_framework import serializers


class ArtistSerializer(serializers.ModelSerializer):
    """A serializer is a class that defines the way that
    an object will be turned into JSON format."""
    class Meta:
        """The Meta class defines the serializer's model and
        the fields that will be returned whenever the object is
        serialized"""
        model = Artist
        # ! notice how we do not include 'id' in the fields
        # this means that although the objects have this attribute
        # it will not be returned in a response. We hide it.
        fields = ('name', 'age', 'genre', 'artwork')
