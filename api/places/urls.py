from django.urls import path, include
import views
from rest_framework import routers

api = routers.SimpleRouter()
api.register(r'places', views.PlaceViewSet)

app_name = 'places'
urlpatterns = [
]
