from django.urls import path

from . import views

app_name = 'syachikuru'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # syachikuru/のURL（トップ画面）
    path('<int:pk>/', views.QuestionView.as_view(), name='question'),
    # syachikuru/pk=question_idのURL（質問画面）
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # syachikuru/pk=question_id/resultsのURL（結果画面）
]