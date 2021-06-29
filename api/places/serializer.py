from rest_framework import serializers

from api.places.models import Places, Images, UserPlaces


class PlacesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Places


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Images


class UserPlacesSerializer(serializers.ModelSerializer):
    place = PlacesSerializer()
    photos = ImageSerializer(many=True, required=False)

    class Meta:
        fields = ('place', 'photos', 'user', 'status', 'date')
        model = UserPlaces

