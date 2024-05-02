from django.urls import path
from .views import music_quiz

urlpatterns = [
    path('', music_quiz, name='music_quiz'),


]