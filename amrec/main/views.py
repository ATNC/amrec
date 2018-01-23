import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from main.models import Category
from main.serializers import CreateCategorySerializer, RetrieveCategorySerializer


class CreateCategoryView(CreateAPIView):
    serializer_class = CreateCategorySerializer
    queryset = Category.objects.all()

    def _create_nested(self, obj, parent=None):
        inst = Category.objects.create(name=obj.get('name'), parent=parent)
        for child in obj.get('children', []):
            self._create_nested(child, parent=inst)

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(self.request.data)
        self._create_nested(serializer.data)
        return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)


class RetrieveCategoryView(RetrieveAPIView):
    serializer_class = RetrieveCategorySerializer
    queryset = Category.objects.all()
