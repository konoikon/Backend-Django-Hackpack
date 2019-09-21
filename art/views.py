from .models import Artist
from rest_framework import status
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import ArtistSerializer


class ArtistView(APIView):

    def get(self, request):
        """This defines the behavior when a GET request is received"""
        # we are pulling all objects of type Artist from the database
        queryset = Artist.objects.all()
        # we are serializing each object (turning it into its JSON format)
        artists = [ArtistSerializer(artist).data for artist in queryset]
        # we are returning the results with an OK status code of 200.
        return JsonResponse({"artists": artists}, status=status.HTTP_200_OK)

    def post(self, request):
        """This defines the behavior when a POST request is received"""
        # A POST request should always carry a payload (the data we need to enter)
        data = request.data
        # we create a new instance of an Artist object with the fields filled in
        # by the data provided in the request
        instance = Artist.objects.create(
            name=data["name"],
            age=data["age"],
            genre=data["genre"],
            artwork=data["artwork"]
        )
        # it is important to save the instance in our database
        instance.save()

        # turning the object into it's JSON format
        serializer = ArtistSerializer(instance)
        # returning the object we created with a Created status of 201
        return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
