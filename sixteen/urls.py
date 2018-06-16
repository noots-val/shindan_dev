from django.urls import path
from .views import QuestionsView, AnimalResultView, PokemonResultView, RpgResultView


app_name = 'sixteen'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('basic_result/pk/', AnimalResultView.as_view(), name='result'),
    path('animal_result/pk/', AnimalResultView.as_view(), name='result'),
    path('pokemon_result/pk/', PokemonResultView.as_view(), name='result'),
    path('rpg_result/pk/', RpgResultView.as_view(), name='result'),
]
