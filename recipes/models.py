from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrates = models.FloatField()

class Menu(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    date = models.DateField()
    meal_type = models.CharField(max_length=50)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)