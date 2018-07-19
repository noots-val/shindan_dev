from django.urls import path
from .views import QuestionsView, ResultView, answer


app_name = 'syachikuru'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('answer/', answer, name='answer'),
    path('result/pk/', ResultView.as_view(), name='result'),
]
