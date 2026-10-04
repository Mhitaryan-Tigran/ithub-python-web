from django.views.generic import TemplateView

from articles.models import Article


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        articles = Article.objects.select_related("author")
        context["lead"] = articles.first()
        context["latest"] = articles[1:4]
        return context
