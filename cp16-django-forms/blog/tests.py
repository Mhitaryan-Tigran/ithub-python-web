from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="testuser", password="secret")
        cls.post = Post.objects.create(title="Тестовая запись", body="Текст записи", author=cls.user)

    def test_model(self):
        self.assertEqual(str(self.post), "Тестовая запись")
        self.assertEqual(self.post.get_absolute_url(), f"/post/{self.post.pk}/")

    def test_list(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "Тестовая запись")
        self.assertGreaterEqual(Post.objects.count(), 4)

    def test_detail(self):
        response = self.client.get(self.post.get_absolute_url())
        self.assertContains(response, "Текст записи")
        self.assertEqual(self.client.get("/post/100000/").status_code, 404)


class FormTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username="author", password="secret")
        cls.post = Post.objects.create(title="Черновик", body="Текст", author=cls.user)

    def test_create(self):
        response = self.client.post(reverse("post_new"), {"title": "Новая", "author": self.user.id, "body": "Тело"})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Post.objects.filter(title="Новая").exists())

    def test_update(self):
        response = self.client.post(reverse("post_edit", args=[self.post.pk]), {"title": "Исправлено", "body": "Новый текст"})
        self.assertEqual(response.status_code, 302)
        self.post.refresh_from_db()
        self.assertEqual(self.post.title, "Исправлено")

    def test_delete(self):
        response = self.client.post(reverse("post_delete", args=[self.post.pk]))
        self.assertRedirects(response, reverse("home"))
        self.assertFalse(Post.objects.filter(pk=self.post.pk).exists())
