from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Result, Characteristic
from .services import CreateQuestionListService, CalculatePointService
from .values import ResultTypeValue
from django.views.generic import ListView, DetailView
from django.urls import reverse
from urllib.parse import quote
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
    result_type = Result.objects.values_list('type', flat=True)
    result_description = Result.objects.values_list('description', flat=True)
    characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)

    response = HttpResponseRedirect(reverse('syachikuru:result', kwargs={'pk': result_id}))
    response.set_cookie('PEACOCKERY_POINT', point_dict['peacockery_point'])
    response.set_cookie('LOYALTIES_POINT', point_dict['loyalties_point'])
    response.set_cookie('ADMISSIBILITY_POINT', point_dict['admissibility_point'])
    response.set_cookie('RESPONSIBILITY_POINT', point_dict['responsibility_point'])
    response.set_cookie('COOPERATIVENESS_POINT', point_dict['cooperativeness_point'])
    response.set_cookie('PEACOCKERY_TYPE', quote(characteristic_types[0]))
    response.set_cookie('LOYALTIES_TYPE', quote(characteristic_types[1]))
    response.set_cookie('ADMISSIBILITY_TYPE', quote(characteristic_types[2]))
    response.set_cookie('RESPONSIBILITY_TYPE', quote(characteristic_types[3]))
    response.set_cookie('COOPERATIVENESS_TYPE', quote(characteristic_types[4]))
    response.set_cookie('RESULT_TYPE', quote(result_type[result_id-1]))
    response.set_cookie('RESULT_DESCRIPTION', quote(result_description[result_id-1]))
    # response.set_cookie('PEACOCKERY_TYPE', 'a')
    # response.set_cookie('LOYALTIES_TYPE', 'b')
    # response.set_cookie('ADMISSIBILITY_TYPE', 'c')
    # response.set_cookie('RESPONSIBILITY_TYPE', 'd')
    # response.set_cookie('COOPERATIVENESS_TYPE', 'e')
    return response


class ResultView(DetailView):
    model = Result
    template_name = 'syachikuru/result.html'

    # def draw_fig(request):
    #     point_dict = request.request.session['point_dict']
    #
    #     plt.rcParams['font.family'] = 'IPAPGothic'  # 全体のフォントを設定
    #
    #     characteristic_types = Characteristic.objects.values_list('characteristic_type', flat=True)
    #
    #     # 軸の作成と設定
    #     number_of_axis = len(characteristic_types)  # 軸数の決定
    #     angle_of_axis = [2 * pi * n / float(number_of_axis) for n in range(number_of_axis)]  # 各軸の角度を計算し値を代入（下2行も併せて）
    #     point_dict += point_dict[:1]
    #     angle_of_axis += angle_of_axis[:1]
    #
    #     plt.rc('axes', linewidth=0.5, edgecolor="#888888")  # 軸の位置とカラーの調整
    #     # ax = plt.figure().add_axes([0.1, 0.1, 0.8, 0.8], polar=True)
    #     characteristic_types_chart = plt.figure(1, figsize=(5, 5))
    #     axis = characteristic_types_chart.add_subplot(111, polar=True)
    #     axis.set_theta_offset(pi / 2)  # 0点を上側に設定
    #     axis.set_theta_direction(-1)  # 基本は反時計回りなので、時計回りに変更
    #     axis.set_rlabel_position(0)  # 軸の値をどこに定めるか（今回なら上側）
    #     axis.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
    #     axis.yaxis.grid(False, color="#888888", linestyle='solid', linewidth=0.5)
    #     plt.xticks(angle_of_axis[:-1], [])  # 「何度」の表示を消すため（x軸の値（動径方向））
    #     plt.yticks([5, 10, 15, 20, 25], ["20%", "40%", "60%", "80%", "100%"])  # 値の範囲設定・・・pointの構造によりけりなのであとで変数で編集
    #
    #     # グラフの見た目の設定
    #     axis.plot(angle_of_axis, point_dict, linewidth=0, linestyle='solid', zorder=1)
    #     axis.fill(angle_of_axis, point_dict, facecolor="#4EE5DA", alpha=1)
    #
    #     # 動径方向の範囲設定・・・pointの構造によりけりなのであとで変数で編集
    #     plt.ylim(0, 25)
    #
    #     # ラベルの位置の設定
    #     for i in range(number_of_axis):
    #         angle_rad = i / float(number_of_axis) * 2 * pi  # piはπ（mathの関数）
    #
    #         if angle_rad == 0:
    #             ha, distance_axis = "center", 3
    #         elif 0 < angle_rad < pi:
    #             ha, distance_axis = "left", 2
    #         elif angle_rad == pi:
    #             ha, distance_axis = "center", 2
    #         else:
    #             ha, distance_axis = "right", 2
    #
    #         axis.text(angle_rad, 25 + distance_axis, characteristic_types[i], size=10,
    #                   horizontalalignment=ha, verticalalignment="center")
    #
    #     canvas = FigureCanvas(characteristic_types_chart)
    #     response = HttpResponse(content_type='image/png')
    #     canvas.print_png(response)
    #     return response
    #
    # """
    #     import logging
    #     for radio_number in range(25):
    #         logging.debug(request.POST["radio" + str(radio_number)])
    # """
