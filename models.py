from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Recipes(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    ingredients = models.TextField(blank=True, verbose_name='Ингредиенты')
    content = models.TextField(blank=True, verbose_name='Приготовление')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменений')
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name='Фотография')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категории')

    def get_absolute_url(self):
        return reverse('recipe_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецепты'
        verbose_name_plural = 'Рецепты'
        ordering = ['-created_at']
