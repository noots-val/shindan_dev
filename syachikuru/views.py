from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice, Result, Characteristic
from django.views.generic import ListView, DetailView
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


def answer(request):
    if request.POST is not None:
        characteristics = Question.objects.values_list('characteristic', flat=True)  # 各質問文のタイプ分けid
        characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)  # 各タイプ（5種類）

        # 各質問文に対応した点数のリストanswersを作成
        answers = []
        for characteristic in range(len(characteristics)):    # POSTデータの取得と得点への変換
            radio_value = int(request.POST["radio" + str(characteristic + 1)])
            point_value = 5 - ((radio_value - 1) % 5)  # point_valueは実際の得点の値:1～5
            answers.append(point_value)

        # 各タイプの得点characteristic_type_pointsを計算
        characteristic_type_points = [0 for i in range(len(characteristic_types))]  # リストの初期化
        for answer in range(len(characteristics)):
            for characteristic_type in range(len(characteristic_types)):
                if characteristics[answer] == characteristic_type + 1:
                    characteristic_type_points[characteristic_type] += answers[answer]
                    break

        # 合計点数ごとにresult_idを選択
        sum_point = sum(characteristic_type_points)
        if sum_point > 75:
            result_id = 1
        elif sum_point > 50:
            result_id = 2
        elif sum_point > 25:
            result_id = 3
        else:
            result_id = 4

        response = HttpResponseRedirect(reverse('syachikuru:result', kwargs={'pk': result_id}))
        response.set_cookie('PEACOCKERY', characteristic_type_points[0])
        response.set_cookie('LOYALTIES', characteristic_type_points[1])
        response.set_cookie('ADMISSIBILITY', characteristic_type_points[2])
        response.set_cookie('RESPONSIBILITY', characteristic_type_points[3])
        response.set_cookie('COOPERATIVENESS', characteristic_type_points[4])
    else:
        return HttpResponseRedirect(reverse('syachikuru:questions'))


class ResultView(DetailView):
    model = Result
    template_name = 'syachikuru/result.html'

    def draw_fig(request):
        from math import pi
        import matplotlib.pyplot as plt
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

        plt.rcParams['font.family'] = 'IPAPGothic'  # 全体のフォントを設定

        characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)
        characteristic_type_points = []
        characteristic_type_points[0] = request.COOKIES['PEACOCKERY']
        characteristic_type_points[1] = request.COOKIES['LOYALTIES']
        characteristic_type_points[2] = request.COOKIES['ADMISSIBILITY']
        characteristic_type_points[3] = request.COOKIES['RESPONSIBILITY']
        characteristic_type_points[4] = request.COOKIES['COOPERATIVENESS']

        # 軸の作成と設定
        N = len(characteristic_types)  # 軸数の決定
        x_as = [2 * pi * n / float(N) for n in range(N)]
        characteristic_type_points += characteristic_type_points[:1]
        x_as += x_as[:1]

        plt.rc('axes', linewidth=0.5, edgecolor="#888888")  # 軸の位置とカラー
        # ax = plt.figure().add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        fig = plt.figure(1, figsize=(5, 5))
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_offset(pi / 2)  # 0点を上側に設定
        ax.set_theta_direction(-1)  # 基本は反時計回りなので、時計回りに変更
        ax.set_rlabel_position(0)  # 軸の値をどこに定めるか（今回なら上側）
        ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
        ax.yaxis.grid(False, color="#888888", linestyle='solid', linewidth=0.5)
        plt.xticks(x_as[:-1], [])  # 「何度」の表示を消すため（x軸の値（動径方向））
        plt.yticks([5, 10, 15, 20, 25], ["20%", "40%", "60%", "80%", "100%"])  # 値の範囲設定・・・pointの構造によりけりなのであとで変数で編集

        # グラフの見た目の設定
        ax.plot(x_as, characteristic_type_points, linewidth=0, linestyle='solid', zorder=1)
        ax.fill(x_as, characteristic_type_points, facecolor="#4EE5DA", alpha=1)

        # 動径方向の範囲設定・・・pointの構造によりけりなのであとで変数で編集
        plt.ylim(0, 25)

        # ラベルの位置の設定
        for i in range(N):
            angle_rad = i / float(N) * 2 * pi

            if angle_rad == 0:
                ha, distance_ax = "center", 3
            elif 0 < angle_rad < pi:
                ha, distance_ax = "left", 2
            elif angle_rad == pi:
                ha, distance_ax = "center", 2
            else:
                ha, distance_ax = "right", 2

            ax.text(angle_rad, 25 + distance_ax, characteristic_types[i], size=10,
                    horizontalalignment=ha, verticalalignment="center")

        canvas = FigureCanvas(fig)
        response = HttpResponse(content_type='image/png')
        canvas.print_png(response)
        return response

    """
        import logging
        for radio_number in range(25):
            logging.debug(request.POST["radio" + str(radio_number)])
    """