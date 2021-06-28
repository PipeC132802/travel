# Create your views here.
from rest_framework import permissions, viewsets

from api.places.models import UserPlaces
from api.places.serializer import PlacesSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.BasePermission, permissions.IsAuthenticated)
    serializer_class = PlacesSerializer
    queryset = UserPlaces.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset
