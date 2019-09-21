from django.urls import path
from .views import ArtistView

urlpatterns = [
    path(r'artists/', ArtistView.as_view(), name='artists')
]
