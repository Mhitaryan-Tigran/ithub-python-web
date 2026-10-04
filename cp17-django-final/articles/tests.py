from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Article, Comment


class NewspaperTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        User = get_user_model()
        cls.author = User.objects.create_user(username="author", password="secret-pass-1")
        cls.other = User.objects.create_user(username="other", password="secret-pass-1")
        cls.article = Article.objects.create(title="Проверка", body="Текст статьи", section="news", author=cls.author)

    def test_pages(self):
        for name in ("home", "article_list", "login", "signup"):
            self.assertEqual(self.client.get(reverse(name)).status_code, 200)
        self.assertContains(self.client.get(self.article.get_absolute_url()), "Текст статьи")

    def test_signup_logs_in(self):
        response = self.client.post(reverse("signup"), {"username": "newbie", "first_name": "Новичок", "email": "n@e.com", "age": 18, "password1": "Strong-pass-77", "password2": "Strong-pass-77"})
        self.assertRedirects(response, reverse("article_list"))
        self.assertEqual(get_user_model().objects.get(username="newbie").age, 18)

    def test_create_requires_login(self):
        self.assertEqual(self.client.get(reverse("article_new")).status_code, 302)
        self.client.login(username="other", password="secret-pass-1")
        self.client.post(reverse("article_new"), {"title": "Моя", "section": "life", "body": "Тело"})
        self.assertEqual(Article.objects.get(title="Моя").author, self.other)

    def test_only_author_edits(self):
        self.client.login(username="other", password="secret-pass-1")
        self.assertEqual(self.client.get(reverse("article_edit", args=[self.article.pk])).status_code, 403)
        self.client.login(username="author", password="secret-pass-1")
        self.assertEqual(self.client.get(reverse("article_edit", args=[self.article.pk])).status_code, 200)

    def test_comment(self):
        self.client.login(username="other", password="secret-pass-1")
        self.client.post(reverse("comment_new", args=[self.article.pk]), {"text": "Отлично"})
        self.assertTrue(Comment.objects.filter(article=self.article, text="Отлично").exists())
