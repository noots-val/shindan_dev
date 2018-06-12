from .models import Question, Choice, Characteristic
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse


class QuestionsView(ListView):
    """
    質問画面用のView
    """
    model = Question
    template_name = 'syachikuru/questions.html'

    def get_context_data(self, **kwargs):
        """
        QuestionテーブルとChoiceテーブルによって、実際に表示するためのリストを作成する

        テーブルを結合せずに冗長なループを行う理由は、
        「質問文 [選択肢1 選択肢2 選択肢3 選択肢4 選択肢5]」というデータの持ち方を実現するため。
        結合させつつ、上記の形で実装する方法があるならばそちらへと変更する

        :return: context
        """
        context = super().get_context_data(**kwargs)
        questions = Question.objects.all()
        choices = Choice.objects.all()

        display_question_list = []
        for question in questions:
            choice_sentences = [choice.choice_sentence for choice in choices if choice.question.pk == question.pk]

            question_dict = {"question_id": question.pk,
                             "question_sentence": question.question_sentence,
                             "choice_sentences": choice_sentences}
            display_question_list.append(question_dict)

        context["display_question_list"] = display_question_list
        return context


class ResultView(ListView):
    model = Question
    template_name = 'syachikuru/result.html'

    def count_characteristic_type(self):
        answers = [3, 5, 5, 5, 5,   # POSTデータの代用
                   5, 5, 5, 5, 5,
                   5, 5, 5, 5, 5
                   ]
        characteristics = Question.objects.values_list('characteristic', flat=True)
        characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)
        characteristic_type_points = []  # characteristic_typeの集計用の変数

        for answer in answers:
            for characteristic_type in characteristic_types:
                if characteristics[answer] == characteristic_type:
                    characteristic_type_points[characteristic_type] += answers[answer]

        return HttpResponseRedirect(reverse('syachikuru:result'))
