from .models import Artist
from rest_framework.views import APIView
from django.http import JsonResponse
from .serializers import ArtistSerializer


class ArtistView(APIView):

    def get(self, request):
        queryset = Artist.objects.all()
        artists = [ArtistSerializer(artist).data for artist in queryset]
        return JsonResponse({"artists": artists})

    def post(self, request):
        data = request.data
        instance = Artist.objects.create(
            name=data["name"],
            age=data["age"],
            genre=data["genre"],
            artwork=data["artwork"]
        )
        instance.save()

        serializer = ArtistSerializer(instance)
        return JsonResponse(serializer.data)
