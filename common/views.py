from django.views.generic import ListView, DetailView

from .models import App, Article


class IndexView(ListView):
    template_name = "common/index.html"
    model = App

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.all().filter(status=1)
        context["article_list"] = articles
        return context


class ArticleView(DetailView):
    template_name = "common/article.html"
    model = Article
