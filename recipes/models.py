from django.db import models

# Create your models here.


class Recipe(models.Model):
    recipeName = models.CharField(max_length=100)
    recipeDescription = models.TextField()
    recipeImage = models.ImageField(
        upload_to='static/images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.recipeName
