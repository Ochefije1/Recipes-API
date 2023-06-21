from django.db import models

# Create your models here.

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')

class Tag(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.ManyToManyField(Recipe, related_name='tags')
