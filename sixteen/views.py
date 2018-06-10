from .models import Question, Choice
from django.views.generic import ListView


class QuestionsView(ListView):
    """
    質問画面用のView
    """
    model = Question
    template_name = 'common/questions.html'

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


class BasicResultView(ListView):
    template_name = 'sixteen/result.html'


class AnimalResultView(ListView):
    template_name = 'sixteen/result.html'


class PokemonResultView(ListView):
    template_name = 'sixteen/result.html'


class RpgResultView(ListView):
    template_name = 'sixteen/result.html'
