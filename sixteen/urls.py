from django.urls import path
from .views import QuestionsView, AnimalResultView


app_name = 'sixteen'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('result/pk/', AnimalResultView.as_view(), name='result'),
]
