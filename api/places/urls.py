from django.urls import path, include
from .views import PlacesViewSet
from rest_framework import routers

api = routers.SimpleRouter()
api.register(r'trips', PlacesViewSet)

app_name = 'places'
urlpatterns = [
    path('', include(api.urls))
]
