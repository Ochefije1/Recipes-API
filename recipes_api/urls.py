"""
URL configuration for recipes_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from api.views import (
    RecipeListCreateView, RecipeRetrieveUpdateDeleteView,
    IngredientListCreateView, IngredientRetrieveUpdateDeleteView,
    TagListCreateView, TagRetrieveUpdateDeleteView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list-create'),
    path('recipes/<int:pk>/', RecipeRetrieveUpdateDeleteView.as_view(),
         name='recipe-retrieve-update-delete'),
    path('recipes/<int:pk>/ingredients/',
         IngredientListCreateView.as_view(), name='ingredient-list-create'),
    path('recipes/<int:recipe_pk>/ingredients/<int:pk>/',
         IngredientRetrieveUpdateDeleteView.as_view(), name='ingredient-retrieve-update-delete'),
    path('recipes/tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('recipes/tags/<int:pk>/', TagRetrieveUpdateDeleteView.as_view(),
         name='tag-retrieve-update-delete'),
]
