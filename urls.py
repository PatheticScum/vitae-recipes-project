from django.urls import path
from .views import *

urlpatterns = [
    path('', RecipesList.as_view(), name='index'),
    path('category/<int:pk>/', RecipesListByCategory.as_view(), name='category_list'),
    path('recipe/<int:pk>', RecipeDetails.as_view(), name='recipe_detail'),
    path('new/', NewRecipe.as_view(), name='add_recipes'),
    path('search/', SearchResults.as_view(), name='search_results'),

]
