from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Result, Characteristic
from .services import CreateQuestionListService, CalculatePointService
from .values import ResultTypeValue
from django.views.generic import ListView, DetailView
from django.urls import reverse
from math import pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

import logging


class QuestionsView(ListView):
    """
    質問画面用のView
    """
    model = Question
    template_name = 'syachikuru/questions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["display_question_list"] = CreateQuestionListService().create_question_list()
        return context


def answer(request):
    point_dict = CalculatePointService().sum_point(request)
    result_id = ResultTypeValue().sort_result_id_by_point(sum(point_dict.values()))
    request.session['point_dict'] = point_dict
    return HttpResponseRedirect(reverse('syachikuru:result', args=(result_id,)))


class ResultView(DetailView):
    model = Result
    template_name = 'syachikuru/result.html'

    def get_context_data(self, **kwargs):
        logging.debug(self.request.session['point_dict'])

    def draw_fig(request):
        plt.rcParams['font.family'] = 'IPAPGothic'  # 全体のフォントを設定

        characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)
        characteristic_types_length = len(characteristic_types)  # タイプの数
        characteristic_type_points = []

        # 軸の作成と設定
        number_of_ax = len(characteristic_types)  # 軸数の決定
        angle_of_ax = [2 * pi * n / float(number_of_ax) for n in range(number_of_ax)]  # 各軸の角度を計算し値を代入（下2行も併せて）
        characteristic_type_points += characteristic_type_points[:1]
        angle_of_ax += angle_of_ax[:1]

        plt.rc('axes', linewidth=0.5, edgecolor="#888888")  # 軸の位置とカラー
        # ax = plt.figure().add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
        fig = plt.figure(1, figsize=(5, 5))
        ax = fig.add_subplot(111, polar=True)
        ax.set_theta_offset(pi / 2)  # 0点を上側に設定
        ax.set_theta_direction(-1)  # 基本は反時計回りなので、時計回りに変更
        ax.set_rlabel_position(0)  # 軸の値をどこに定めるか（今回なら上側）
        ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
        ax.yaxis.grid(False, color="#888888", linestyle='solid', linewidth=0.5)
        plt.xticks(angle_of_ax[:-1], [])  # 「何度」の表示を消すため（x軸の値（動径方向））
        plt.yticks([5, 10, 15, 20, 25], ["20%", "40%", "60%", "80%", "100%"])  # 値の範囲設定・・・pointの構造によりけりなのであとで変数で編集

        # グラフの見た目の設定
        ax.plot(angle_of_ax, characteristic_type_points, linewidth=0, linestyle='solid', zorder=1)
        ax.fill(angle_of_ax, characteristic_type_points, facecolor="#4EE5DA", alpha=1)

        # 動径方向の範囲設定・・・pointの構造によりけりなのであとで変数で編集
        plt.ylim(0, 25)

        # ラベルの位置の設定
        for i in range(number_of_ax):
            angle_rad = i / float(number_of_ax) * 2 * pi

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
