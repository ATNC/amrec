from rest_framework import serializers
from rest_framework_recursive.fields import RecursiveField

from main.models import Category


class CreateCategorySerializer(serializers.Serializer):
    name = serializers.CharField()
    children = serializers.ListField(RecursiveField())


class CategoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',

        )


class RetrieveCategorySerializer(serializers.ModelSerializer):
    children = CategoryItemSerializer(source='get_children', many=True)
    siblings = CategoryItemSerializer(source='get_siblings', many=True)
    parents = CategoryItemSerializer(source='get_parents', many=True)

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'children',
            'siblings',
            'parents'
        )
