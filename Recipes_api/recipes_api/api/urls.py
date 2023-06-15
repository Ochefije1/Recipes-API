from django.urls import path, include
from rest_framework import routers
from .views import RecipeViewSet, IngredientViewSet, TagViewSet


router = routers.DefaultRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('api/', TemplateView.as_view(template_name='recipes.html')),
]

