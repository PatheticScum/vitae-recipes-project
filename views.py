from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Recipes, Category
from .forms import RecipeForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.db.models import Q


class RecipesList(ListView):
    model = Recipes
    context_object_name = 'recipes'
    template_name = 'blog/all_recipes.html'
    paginate_by = 3

    def get_queryset(self):
        return Recipes.objects.filter(is_published=True)


class RecipesListByCategory(RecipesList):
    def get_queryset(self):
        return Recipes.objects.filter(
            category_id=self.kwargs['pk'],
            is_published=True

        ).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        category = Category.objects.get(pk=self.kwargs['pk'])
        context['title'] = category.title
        return context


class RecipeDetails(DetailView):
    model = Recipes
    template_name = 'blog/details.html'

    def get_queryset(self):
        return Recipes.objects.filter(pk=self.kwargs['pk'], is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        recipe = Recipes.objects.get(pk=self.kwargs['pk'])
        context['title'] = recipe.title
        context['ingredients'] = recipe.ingredients
        context['content'] = recipe.content
        return context


class NewRecipe(CreateView):
    form_class = RecipeForm
    template_name = 'blog/add_recipes.html'
    extra_context = {
        'title': 'Добавить Рецепт'
    }

    success_url = reverse_lazy('index')


class SearchResults(RecipesList):
    def get_queryset(self):
        word = self.request.GET.get('q')
        recipes = Recipes.objects.filter(
            Q(title__icontains=word) | Q(content__icontains=word), is_published=True
        )
        return recipes
