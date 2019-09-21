from django.urls import path
from .views import ArtistView

urlpatterns = [
    # we define the endpoint (http://localhost:8000/artists/)
    # we can then access this with appropriate request types (GET, POST)
    # depending on the request type it will behave according to the view
    # that we specified in views.py
    path(r'artists/', ArtistView.as_view(), name='artists')
]
