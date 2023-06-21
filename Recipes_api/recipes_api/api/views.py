from django.shortcuts import render
from rest_framework import generics, viewsets
from api.models import Recipe, Ingredient, Tag
from api.serializers import RecipeSerializer, IngredientSerializer, TagSerializer

# Create your views here.


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


