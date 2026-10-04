from django.db import models


class Post(models.Model):
    CATEGORIES = [("sell", "Продам"), ("buy", "Куплю"), ("service", "Услуги"), ("lost", "Потеряно и найдено")]

    title = models.CharField("Заголовок", max_length=120)
    text = models.TextField("Текст")
    category = models.CharField("Раздел", max_length=10, choices=CATEGORIES, default="sell")
    price = models.PositiveIntegerField("Цена, ₽", null=True, blank=True)
    contact = models.CharField("Контакт", max_length=60)
    created = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ["-created"]
        verbose_name = "объявление"
        verbose_name_plural = "объявления"

    def __str__(self):
        return self.title
