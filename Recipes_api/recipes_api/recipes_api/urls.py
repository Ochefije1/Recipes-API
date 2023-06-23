
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from api.views import *


router = routers.DefaultRouter()
router.register('recipe', RecipeViewSet)
router.register('ingredient', IngredientViewSet)
router.register('tag', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
