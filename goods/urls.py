UkrKraft_2025_name='goods'
from django.urls import path

from goods import views

app_name = 'goods'  # Визначення простору імен

urlpatterns = [
    path('', views.catalog, name='index'),
    path('product/<int:product_id>/', views.product, name='product'),

]
