from django.urls import path
from . import views
#from .views import music_quiz

urlpatterns = [
    path('', views.music_quiz, name='music_quiz'),


]


