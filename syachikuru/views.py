from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = 'syachikuru/index.html'
    context_object_name = 'latest_question_list'


class QuestionView(generic.DetailView):
    model = Question
    template_name = 'syachikuru/question.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'syachikuru/results.html'
