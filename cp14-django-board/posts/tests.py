from django.test import TestCase
from django.urls import reverse

from .models import Post


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(title="Тестовое объявление", text="Текст", category="buy", price=100, contact="@test")

    def test_model(self):
        self.assertEqual(str(self.post), "Тестовое объявление")
        self.assertEqual(self.post.get_category_display(), "Куплю")

    def test_home(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Тестовое объявление")
        self.assertTemplateUsed(response, "home.html")

    def test_filter(self):
        self.assertNotContains(self.client.get(reverse("home") + "?category=sell"), "Тестовое объявление")
