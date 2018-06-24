from django.urls import path
from .views import QuestionsView, answer, BasicResultView, AnimalResultView, PokemonResultView, RpgResultView


app_name = 'sixteen'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('answer/', answer, name='answer'),
    path('basic_result/<str:result_type>/', BasicResultView.as_view(), name='basic_result'),
    path('animal_result/<str:result_type>/', AnimalResultView.as_view(), name='animal_result'),
    path('pokemon_result/<str:result_type>/', PokemonResultView.as_view(), name='pokemon_result'),
    path('rpg_result/<str:result_type>/', RpgResultView.as_view(), name='rpg_result'),
]
