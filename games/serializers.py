from rest_framework import serializers
from .models import Genre, Game, Review



class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class GameSerializer(serializers.ModelSerializer):
    platform = serializers.CharField(source='get_platform_display')  # Use get_platform_display for displaying platform choices
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = '__all__'

