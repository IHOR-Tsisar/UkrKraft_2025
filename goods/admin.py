from django.contrib import admin

from .models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slag':('name',)}
    list_display = ['name', 'slag', 'isvisible']
    list_filter = ['isvisible']
    search_fields = ['name', 'slag']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields ={'slag':('name',)}
    list_display = ['name', 'category', 'price', 'quantity', 'isvisible']
    list_filter = ['category', 'isvisible']
    search_fields = ['name', 'slag', 'category__name']
