from django.urls import path
from .views import IndexView, ArticleView

urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('article/<int:pk>/', ArticleView.as_view(), name='article'),
]
