# Create your views here.
from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from api.places.models import UserPlaces, Places, Images
from api.places.serializer import UserPlacesSerializer


class PlacesViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.BasePermission, permissions.IsAuthenticated)
    serializer_class = UserPlacesSerializer
    queryset = UserPlaces.objects.all()

    def get_queryset(self):
        queryset = self.queryset
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        validated_data = request.data
        validated_data["user"] = request.user
        place_dic = validated_data.pop('place')
        photos_data = validated_data.pop('photos')
        place, created = Places.objects.get_or_create(**place_dic)
        validated_data["place"] = place
        user_place, _ = UserPlaces.objects.get_or_create(**validated_data)

        for img in photos_data:
            photo, _ = Images.objects.get_or_create(**img)
            user_place.photos.add(photo)

        user_place.place = place
        user_place.save()
        return Response(UserPlacesSerializer(user_place).data)

    def partial_update(self, request, *args, **kwargs):
        photos_data = request.data.pop("photos")
        user_place = get_object_or_404(self.get_queryset(), pk=kwargs["pk"])
        photos_list = []
        for img in photos_data:
            photo, _ = Images.objects.get_or_create(**img)
            photos_list.append(photo)
        user_place.photos.set(photos_list)
        return super().partial_update(request, *args, **kwargs)
