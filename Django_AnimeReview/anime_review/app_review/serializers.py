from rest_framework import serializers
from app_review.models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Allboard
        fields = ('id', 'name', 'address', 'photo', 'tags', 'menu', 'pub_date')


