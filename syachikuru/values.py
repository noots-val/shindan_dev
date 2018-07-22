from enum import Enum

ERROR_MESSAGE = 'しばらく経ってもエラーが解消しない場合、管理者にご報告していただけると幸いです。'


class CharacteristicValue:
    PEACOCKERY = 1
    LOYALTIES = 2
    ADMISSIBILITY = 3
    RESPONSIBILITY = 4
    COOPERATIVENESS = 5

    def is_peacockery(self, question_characteristic):
        if self.PEACOCKERY == question_characteristic:
            return True
        else:
            return False

    def is_loyalties(self, question_characteristic):
        if self.LOYALTIES == question_characteristic:
            return True
        else:
            return False

    def is_admissibility(self, question_characteristic):
        if self.ADMISSIBILITY == question_characteristic:
            return True
        else:
            return False

    def is_responsibility(self, question_characteristic):
        if self.RESPONSIBILITY == question_characteristic:
            return True
        else:
            return False

    def is_cooperativeness(self, question_characteristic):
        if self.COOPERATIVENESS == question_characteristic:
            return True
        else:
            return False


class ResultTypeValue:
    ANT = 1
    TORTOISE = 2
    RABBIT = 3
    BUSH_CRICKET = 4

    def __init__(self):
        self.ant_border = 75
        self.tortoise_border = 50
        self.rabbit_border = 25
        self.bush_cricket_border = 0  # 使わないが一応定義

    def sort_result_id_by_point(self, sum_point):
        """
        合計点数でresult_idを振り分け

        :param sum_point:
        :return result_id:
        """

        if sum_point > self.ant_border:
            return ResultTypeValue.ANT
        elif sum_point > self.tortoise_border:
            return ResultTypeValue.TORTOISE
        elif sum_point > self.rabbit_border:
            return ResultTypeValue.RABBIT
        else:
            return ResultTypeValue.BUSH_CRICKET
