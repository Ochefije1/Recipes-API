from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from api.models import Recipe, Ingredient, Tag
from api.serializers import RecipeSerializer, IngredientSerializer, TagSerializer

from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


@api_view(['POST'])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_all_recipes(request):
    recipes = Recipe.objects.all()
    serializer = RecipeSerializer(recipes, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(recipe)
    return Response(serializer.data)


@api_view(['PUT'])
def update_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = RecipeSerializer(recipe, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return Response(status=204)


@api_view(['GET'])
def get_recipe_ingredients(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ingredients = recipe.ingredients.all()
    serializer = IngredientSerializer(ingredients, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_ingredient(request, recipe_pk, ingredient_pk):
    ingredient = get_object_or_404(
        Ingredient, recipe=recipe_pk, pk=ingredient_pk)
    serializer = IngredientSerializer(ingredient)
    return Response(serializer.data)


@api_view(['POST'])
def create_ingredient(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    serializer = IngredientSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(recipe=recipe)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_ingredient(request, recipe_pk, ingredient_pk):
    ingredient = get_object_or_404(
        Ingredient, recipe=recipe_pk, pk=ingredient_pk)
    serializer = IngredientSerializer(ingredient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['GET'])
def get_recipe_tags(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    tags = recipe.tags.all()
    serializer = TagSerializer(tags, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def get_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    serializer = TagSerializer(tag)
    return Response(serializer.data)


@api_view(['POST'])
def create_tag(request):
    serializer = TagSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)


@api_view(['PUT'])
def update_tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    serializer = TagSerializer(tag, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)


@api_view(['DELETE'])
def delete_tag(request, pk):
    tag = get_object_or_404
