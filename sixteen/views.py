from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, DetailView
from django.db.models import Q
from django.db import transaction
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
import logging

from .models import Question, Choice, Type, Answer, TypeFunction, Anime, AnimalResult, PokemonResult, Pokemon, RpgResult
from .enum import ProductId, QuestionCategory

from common.models import App, Article


class QuestionsView(TemplateView):
    """
    質問画面用のView
    """
    template_name = 'sixteen/questions.html'

    def get_context_data(self, **kwargs):
        """
        質問とそれに紐づく選択肢のリストを返すメソッド
        質問と選択肢のリスト（display_question_list）を作成→パラメータからproduct_idを取得→contextをreturn

        :param kwargs:
        :return: context(display_question_list, product_id, error_message)
        """
        context = super().get_context_data(**kwargs)

        try:
            questions = Question.objects.all().values()
            choices = Choice.objects.all().values()
        except ObjectDoesNotExist:
            context['error_message'] = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
            return context

        display_question_list = []
        for question in questions:
            choices_of_question = [choice for choice in choices if choice['question_id'] == question['id']]

            question_dict = {'question_id': question['id'],
                             'question_sentence': question['question_sentence'],
                             'choices_of_question': choices_of_question}
            display_question_list.append(question_dict)

        context['display_question_list'] = display_question_list

        try:
            context['product_id'] = self.request.GET['product_id']

        except (AttributeError, MultiValueDictKeyError) as error:
            context['product_id'] = ProductId.BASIC.value
        finally:
            return context


class BasicResultView(DetailView):
    template_name = 'sixteen/basic_result.html'

    def get_object(self, queryset=None):
            return Type.objects.get(name=self.kwargs['result_type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['typefunction_list'] = TypeFunction.objects.all().prefetch_related('function').filter(
                type__name=self.kwargs['result_type'])
            context['anime_list'] = Anime.objects.all().prefetch_related('type').filter(
                type__name=self.kwargs['result_type'])

            context['article_list'] = Article.objects.filter(Q(id='6') | Q(id='7')).values()
            context['app_list'] = App.objects.filter(category='sixteen').values()

        except ObjectDoesNotExist:
            context['error_message'] = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
        finally:
            return context


class AnimalResultView(DetailView):
    template_name = 'sixteen/animal_result.html'

    def get_object(self, queryset=None):
        return Type.objects.get(name=self.kwargs['result_type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['animal_result'] = AnimalResult.objects.all().filter(type__name=self.kwargs['result_type']).get()

            context['anime_list'] = Anime.objects.all().prefetch_related('type').filter(
                type__name=self.kwargs['result_type'])

            context['article_list'] = Article.objects.filter(Q(id='6') | Q(id='7')).values()
            context['app_list'] = App.objects.filter(category='sixteen').values()

        except ObjectDoesNotExist:
            context['error_message'] = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
        finally:
            return context


class PokemonResultView(DetailView):
    template_name = 'sixteen/pokemon_result.html'

    def get_object(self, queryset=None):
        return Type.objects.get(name=self.kwargs['result_type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['pokemon_result'] = PokemonResult.objects.all().filter(type__name=self.kwargs['result_type']).get()

            context['pokemon_list'] = Pokemon.objects.all().prefetch_related('type').filter(
                type__name=self.kwargs['result_type'])

            context['article_list'] = Article.objects.filter(Q(id='6') | Q(id='7')).values()
            context['app_list'] = App.objects.filter(category='sixteen').values()

        except ObjectDoesNotExist:
            context['error_message'] = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
        finally:
            return context


class RpgResultView(DetailView):
    template_name = 'sixteen/rpg_result.html'

    def get_object(self, queryset=None):
        return Type.objects.get(name=self.kwargs['result_type'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        try:
            context['rpg_result'] = RpgResult.objects.all().filter(type__name=self.kwargs['result_type']).get()

            context['anime_list'] = Anime.objects.all().prefetch_related('type').filter(
                type__name=self.kwargs['result_type'])

            context['article_list'] = Article.objects.filter(Q(id='6') | Q(id='7')).values()
            context['app_list'] = App.objects.filter(category='sixteen').values()

        except ObjectDoesNotExist:
            context['error_message'] = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
        finally:
            return context


@transaction.atomic
def answer(request):
    """
    質問画面で選択された結果を集計する関数
    選択結果取得と集計→性格型を決定→Answerテーブルにインサート→結果画面にリダイレクト

    :param request:
    :return:
    """
    ie_point = sn_point = ft_point = jp_point = 0

    def sort_point_by_category(point, category_of_question):
        """
        点数振り分けを行う関数内関数

        :param point:
        :param category_of_question:
        :return:
        """
        str_question_category = str(category_of_question)
        if str_question_category == QuestionCategory.IE.value:
            nonlocal ie_point
            ie_point += point
        elif str_question_category == QuestionCategory.SN.value:
            nonlocal sn_point
            sn_point += point
        elif str_question_category == QuestionCategory.FT.value:
            nonlocal ft_point
            ft_point += point
        elif str_question_category == QuestionCategory.JP.value:
            nonlocal jp_point
            jp_point += point

    try:

        target_product = request.POST['target_product']
        questions = Question.objects.all().values()
        choices = Choice.objects.all().values()

        # 質問ごとに選択結果を取得、選択肢テーブルのidから得点を取得して振り分け
        for question in questions:
            selected_value = request.POST['radio' + str(question['id'])]
            [sort_point_by_category(choice['point'], question['category']) for choice in choices if
             int(selected_value) == choice['id']]

        first_character = 'I' if ie_point >= 0 else 'E'
        second_character = 'S' if sn_point >= 0 else 'N'
        third_character = 'F' if ft_point >= 0 else 'T'
        fourth_character = 'J' if jp_point >= 0 else 'P'
        result_type = first_character + second_character + third_character + fourth_character

        target_type = Type.objects.get(name=result_type)
        with transaction.atomic():
            for question in questions:
                selected_value = request.POST['radio' + str(question['id'])]
                Answer(question_id=question['id'], choice_id=selected_value, type_id=target_type.pk).save()

    except (AttributeError, MultiValueDictKeyError, ObjectDoesNotExist) as error:
        request.session['error_message'] = '集計に失敗しました。\nしばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'
        return HttpResponseRedirect(reverse('index'))
    else:
        if target_product == ProductId.BASIC.value:
            return HttpResponseRedirect(reverse('sixteen:basic_result', kwargs={'result_type': result_type}))
        elif target_product == ProductId.ANIMAL.value:
            return HttpResponseRedirect(reverse('sixteen:animal_result', kwargs={'result_type': result_type}))
        elif target_product == ProductId.POKEMON.value:
            return HttpResponseRedirect(reverse('sixteen:pokemon_result', kwargs={'result_type': result_type}))
        elif target_product == ProductId.RPG.value:
            return HttpResponseRedirect(reverse('sixteen:rpg_result', kwargs={'result_type': result_type}))
