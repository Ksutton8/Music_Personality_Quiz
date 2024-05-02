from django.urls import path
#from . import views
from .views import music_quiz

urlpatterns = [
    path('', music_quiz, name='music_quiz'),


]