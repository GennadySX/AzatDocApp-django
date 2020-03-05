from rest_framework import serializers
from api.models import *


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'desc',
        )
        model = Category


class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'category_id',
            'name',
            'desc',
        )
        model = Theme


class DetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'theme_id',
            'detail',
        )
        model = Detail
