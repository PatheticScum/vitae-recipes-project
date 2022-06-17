from django.contrib import admin

from .models import Recipes, Category


class RecipesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'created_at', 'is_published')
    list_display_links = ('title', )
    list_editable = ('is_published', )


admin.site.register(Recipes, RecipesAdmin)
admin.site.register(Category)
