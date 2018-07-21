from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('restaurants/',views.Restaurants, name = 'restaurants'),
    path('addRestaurants/', views.add_rest, name = 'addRestaurants'),
    path('restaurant/<int:id>', views.restaurant, name = 'restaurant'),
    path('review/<int:id>', views.review, name = 'review')
]