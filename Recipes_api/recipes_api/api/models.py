from django.db import models


# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    time = models.IntegerField()

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    descriptions = models.TextField()
    quantity = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name
