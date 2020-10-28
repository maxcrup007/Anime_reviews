from rest_framework import serializers
from food.models import Restaurant


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allboard
        fields = ('id', 'category', 'header', 'date', 'status_ongoing', 'favor', 'detail', 'reviews')