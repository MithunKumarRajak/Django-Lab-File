from recipes.views import *
from django.urls import path

urlpatterns = [
    path('', recipe, name='recipe'),
]
