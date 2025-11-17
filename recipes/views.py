from .forms import RecipeForm
from django.shortcuts import render, redirect, get_object_or_404
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


# templates CRUD Operations
# Create
def add_recipe(request):
    form = RecipeForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('list_recipes')
    return render(request, 'templates/recipes/add_recipe.html', {'form': form})

# Read


def list_recipes(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/list_recipes.html', {'recipes': recipes})

# Update


def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('list_recipes')
    return render(request, 'recipes/edit_recipe.html', {'form': form})

# Delete


def delete_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('list_recipes')
    return render(request, 'recipes/delete_recipe.html', {'recipe': recipe})
