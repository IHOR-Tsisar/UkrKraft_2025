UkrKraft_2025_name='goods'
from django.urls import path

from goods import views

app_name = 'goods'  # Визначення простору імен

urlpatterns = [
    path('<slug:category_slug>/', views.catalog, name='index'),
    path('product/<slug:product_slug>/', views.product, name='product'),

]
