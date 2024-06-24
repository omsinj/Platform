# games/urls.py

from django.urls import path
from . import views

app_name = 'games'  # Namespace definition

urlpatterns = [
    path('', views.home, name='home'),
    path('games/', views.games_menu, name='games'),
    path('games/', views.games_menu, name='games_menu'),
    path('resources/', views.resources_menu, name='resources'),
    path('games/system-generated/', views.system_generated, name='system_generated'),
    path('games/system-generated/<int:category_id>/levels/', views.category_levels, name='category_levels'),
    path('games/system-generated/<int:category_id>/levels/<int:level_id>/', views.play_level, name='play_level'),
    path('add_question/', views.add_question, name='add_question'),
    path('rewards/', views.rewards, name='rewards'),
]



