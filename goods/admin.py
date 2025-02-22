from django.contrib import admin

from .models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name', 'slug', 'isvisible']
    list_filter = ['isvisible']
    search_fields = ['name', 'slug']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slug':('name',)}
    list_display = ['name', 'category', 'price', 'quantity','slug', 'isvisible']
    list_filter = ['category', 'isvisible']
    search_fields = ['name', 'slug', 'category__name']
