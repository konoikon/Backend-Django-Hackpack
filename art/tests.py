from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Artist


class HackpackTests(APITestCase):

    def test_create_artist(self):
        url = reverse('artists')
        data = {'name': 'Salvador Dali',
                'age': 115,
                'genre': 'surrealism',
                'artwork': 'The Persistence of Memory'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Artist.objects.count(), 1)
        self.assertEqual(Artist.objects.get().name, 'Salvador Dali')

    def test_get_artist(self):
        url = reverse('artists')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
