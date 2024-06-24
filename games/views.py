from django.shortcuts import render, get_object_or_404
from .models import Category, Level, Reward, Question
from .ai_service import classify_question
import numpy as np

def home(request):
    return render(request, 'home.html')

def games_menu(request):
    return render(request, 'games_menu.html')

def resources_menu(request):
    return render(request, 'resources.html')

def system_generated(request):
    categories = Category.objects.all()
    return render(request, 'system_generated.html', {'categories': categories})

def system_generated_game(request):
    if request.method == 'POST':
        # Example input features (replace with actual user input processing)
        input_features = np.random.rand(3)  # Example feature vector
        difficulty = classify_question(input_features)
        return render(request, 'game.html', {'difficulty': difficulty})
    return render(request, 'game.html')

def category_levels(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    levels = Level.objects.all()
    return render(request, 'levels.html', {'category': category, 'levels': levels})

def play_level(request, category_id, level_id):
    category = get_object_or_404(Category, id=category_id)
    level = get_object_or_404(Level, id=level_id)
    questions = Question.objects.filter(category=category, level=level)
    return render(request, 'play_level.html', {'category': category, 'level': level, 'questions': questions})

def add_question(request):
    if request.method == 'POST':
        question_text = request.POST.get('question')
        category_id = request.POST.get('category_id')
        level = classify_question(question_text)  # Assuming classify_question returns level name
        category = get_object_or_404(Category, id=category_id)
        Question.objects.create(text=question_text, category=category, level=Level.objects.get(name=level))
    categories = Category.objects.all()
    return render(request, 'add_question.html', {'categories': categories})

def rewards(request):
    rewards = Reward.objects.all()
    return render(request, 'rewards.html', {'rewards': rewards})


def game_view(request):
    if request.method == 'POST':
        user_question = request.POST.get('question')  # Example: get user question from form
        predicted_difficulty = classify_question(user_question)
        return render(request, 'game.html', {'predicted_difficulty': predicted_difficulty})
    else:
        return render(request, 'game.html')

def home(request):
    return render(request, 'home.html')

def games_menu(request):
    return render(request, 'games_menu.html')

def system_generated_games(request):
    return render(request, 'system_generated_games.html')

def user_generated_games(request):
    return render(request, 'user_generated_games.html')

def system_generated_game_details(request, category, play_mode):
    # Example of handling parameters
    return render(request, 'system_generated_game_details.html', {'category': category, 'play_mode': play_mode})

def resources_menu(request):
    return render(request, 'resources_menu.html')