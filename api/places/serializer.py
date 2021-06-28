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


class TravellersSerializer(serializers.ModelSerializer):
    place = PlacesSerializer(read_only=True)
    modules = ImageSerializer(many=True)

    class Meta:
        fields = '__all__'
        model = UserPlaces
