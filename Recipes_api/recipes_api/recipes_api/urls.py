
from django.contrib import admin
from django.urls import path, include
from api.views import (
    recipe_list,
    recipe_detail,
    ingredient_list,
    ingredient_detail,
    tag_list,
    tag_create,
    tag_detail,
)

urlpatterns = [
    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),
    path('recipes/<int:recipe_pk>/ingredients/', ingredient_list, name='ingredient-list'),
    path('recipes/<int:recipe_pk>/ingredients/<int:ingredient_pk>/', ingredient_detail, name='ingredient-detail'),
    path('recipes/tags/', tag_list, name='tag-list'),
    path('recipes/tags/<int:pk>/', tag_detail, name='tag-detail'),
    path('recipes/tags/create/', tag_create, name='tag-create'),
]



