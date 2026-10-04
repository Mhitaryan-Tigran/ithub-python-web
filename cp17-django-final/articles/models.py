from django.conf import settings
from django.db import models
from django.urls import reverse


class Article(models.Model):
    SECTIONS = [("news", "Новости"), ("study", "Учёба"), ("life", "Студенческая жизнь"), ("tech", "Технологии")]

    title = models.CharField("Заголовок", max_length=200)
    section = models.CharField("Рубрика", max_length=10, choices=SECTIONS, default="news")
    body = models.TextField("Текст")
    date = models.DateTimeField("Дата", auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="articles", verbose_name="Автор")

    class Meta:
        ordering = ["-date"]
        verbose_name = "статья"
        verbose_name_plural = "статьи"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"pk": self.pk})


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="comments")
    text = models.CharField("Комментарий", max_length=500)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return self.text[:40]
