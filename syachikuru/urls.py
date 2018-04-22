from django.urls import path
from .views import QuestionsView, ResultView


app_name = 'syachikuru'
urlpatterns = [
    path('questions/', QuestionsView.as_view(), name='questions'),
    path('result/pk/', ResultView.as_view(), name='result'),
]
