from django.views.generic import ListView

from .models import Post


class HomePageView(ListView):
    model = Post
    template_name = "home.html"

    def get_queryset(self):
        category = self.request.GET.get("category")
        qs = super().get_queryset()
        return qs.filter(category=category) if category else qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Post.CATEGORIES
        context["active"] = self.request.GET.get("category")
        return context
