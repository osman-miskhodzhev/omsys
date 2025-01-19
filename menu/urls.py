from django.urls import path

from .views import MenuView, FoodAdd

app_name = 'menu'

urlpatterns = [
    path('', MenuView.as_view(), name='menu-list'),
    path('food_add/', FoodAdd.as_view(), name='food-add'),
]