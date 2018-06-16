from django.http import HttpResponseRedirect, HttpRequest
from django.urls import reverse

from .models import Question, Choice, Result, Characteristic
from django.views.generic import ListView, DetailView


class QuestionsView(ListView):
    """
    質問画面用のView
    """
    model = Question
    template_name = 'syachikuru/questions.html'

    def get_context_data(self, **kwargs):
        """
        QuestionテーブルとChoiceテーブルによって、実際に表示するためのリストを作成する
        :return: context
        """
        context = super().get_context_data(**kwargs)
        questions = Question.objects.all()
        choices = Choice.objects.all()

        display_question_list = []
        for question in questions:
            choices_of_question = [choice for choice in choices if choice.question.pk == question.pk]

            question_dict = {"question_id": question.pk,
                             "question_sentence": question.question_sentence,
                             "choices_of_question": choices_of_question}
            display_question_list.append(question_dict)

        context["display_question_list"] = display_question_list
        return context


class ResultView(DetailView):
    model = Result
    template_name = 'syachikuru/result.html'

    def calculate_characteristic_type(request):
        characteristics = Question.objects.values_list('characteristic', flat=True)
        characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)
        answers = []
        for radio_number in range(characteristics):    # POSTデータの取得
            answers[radio_number] = request.POST["radio" + str(radio_number)]
        characteristic_type_points = []  # characteristic_typeの集計用の変数

        for answer in range(answers):  # 各得点の計算
            for characteristic_type in range(len(characteristic_types)):
                if characteristics[answer] == characteristic_type + 1:
                    characteristic_type_points[characteristic_type] += answers[answer]

        return characteristic_type_points


def answer(request):
    if request.POST is not None:
        # ここに処理を書く
        return HttpResponseRedirect(reverse('syachikuru:result', kwargs={'pk': "1"}))
    else:
        return HttpResponseRedirect(reverse('syachikuru:questions'))
