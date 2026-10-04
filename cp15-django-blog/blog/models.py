from django.conf import settings
from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField("Заголовок", max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Автор")
    body = models.TextField("Текст")
    created = models.DateTimeField("Опубликовано", auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "запись"
        verbose_name_plural = "записи"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})
