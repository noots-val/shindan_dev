from .models import Question, Choice
from .values import CharacteristicValue


class CreateQuestionListService:
    """
    QuestionテーブルとChoiceテーブルによって、質問と選択肢を紐づけたリストを作成する
    :return: context
    """

    def __init__(self):
        self.questions = Question.objects.all().values()
        self.choices = Choice.objects.all().values()

    def create_question_list(self):
        display_question_list = []
        for question in self.questions:
            choices_of_question = [choice for choice in self.choices if choice['question_id'] == question['id']]

            question_dict = {'question_id': question['id'],
                             'question_sentence': question['question_sentence'],
                             'choices_of_question': choices_of_question}
            display_question_list.append(question_dict)

        return display_question_list


class CalculatePointService:

    def __init__(self):
        self.questions = Question.objects.all().values()
        self.choices = Choice.objects.all().values()

        self.peacockery_point = self.loyalties_point = self.admissibility_point = self.responsibility_point = self.cooperativeness_point = 0

    def sum_point(self, request):
        for question in self.questions:
            selected_value = request.POST['radio' + str(question['id'])]
            [self.sort_point_by_characteristic(choice['point'], question['characteristic_id'])
             for choice in self.choices if int(selected_value) == choice['id']]

        point_dict = {'peacockery_point': self.peacockery_point,
                      'loyalties_point': self.loyalties_point,
                      'admissibility_point': self.admissibility_point,
                      'responsibility_point': self.responsibility_point,
                      'cooperativeness_point': self.cooperativeness_point}

        return point_dict

    def sort_point_by_characteristic(self, point, characteristic_of_question):
        """
        点数振り分けを行うメソッド

        :param point:
        :param characteristic_of_question:
        :return:
        """

        if CharacteristicValue().is_peacockery(characteristic_of_question):
            self.peacockery_point += point
        elif CharacteristicValue().is_loyalties(characteristic_of_question):
            self.loyalties_point += point
        elif CharacteristicValue().is_admissibility(characteristic_of_question):
            self.admissibility_point += point
        elif CharacteristicValue().is_responsibility(characteristic_of_question):
            self.responsibility_point += point
        elif CharacteristicValue().is_cooperativeness(characteristic_of_question):
            self.cooperativeness_point += point
