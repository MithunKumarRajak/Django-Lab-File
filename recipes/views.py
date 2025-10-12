from django.shortcuts import render, redirect
from .models import Recipe

# frontend se backend ko data bhejna hai toh humein POST request use karni hogi


def recipe(request):
    if request.method == 'POST':
        data = request.POST
        recipeName = data.get('recipeName')
        recipeDescription = data.get('recipeDescription')
        recipeImage = request.FILES.get('recipeImage')
        Recipe.objects.create(
            recipeName=recipeName,
            recipeDescription=recipeDescription,
            recipeImage=recipeImage
        )

        """redirect to the same page after submission Or --> return redirect('recipe') Dono kaam karta hai"""
        return redirect('/recipe/')
    return render(request, 'recipes/recipe.html')
