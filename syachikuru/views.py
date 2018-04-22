from .models import Question
from django.views.generic import ListView


class QuestionsView(ListView):
    model = Question
    template_name = 'syachikuru/questions.html'

    def get_queryset(self):
        return Question


class ResultView(ListView):
    model = Question
    template_name = 'syachikuru/result.html'
