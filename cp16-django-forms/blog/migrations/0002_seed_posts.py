from django.contrib.auth.hashers import make_password
from django.db import migrations

POSTS = [
    ("Почему Django, а не Flask", "Flask даёт свободу: маршрут, функция, шаблон — и сайт готов. Django решает больше за тебя: админка, ORM, миграции и формы уже внутри.\n\nДля маленького сервиса я бы взял Flask, а для проекта с пользователями и базой — Django: меньше кода, который пишешь сам."),
    ("ORM за пять минут", "Модель — это класс, поле — атрибут, а миграция — история изменений базы.\n\nPost.objects.all() превращается в SELECT, а makemigrations сам понимает, какие таблицы нужно создать или изменить. SQL при этом никуда не делся: его полезно посмотреть через print(queryset.query)."),
    ("Шаблоны и наследование", "Общий каркас страницы лежит в base.html, а каждая страница заполняет только свой блок content.\n\nТак шапка и подвал живут в одном месте, и изменить их можно одной правкой."),
    ("Статические файлы", "CSS, картинки и скрипты Django ищет в папках static. В шаблоне их подключает тег static, а в настройках достаточно указать STATICFILES_DIRS.\n\nНа сервере все файлы собирает в одно место команда collectstatic."),
]


def seed(apps, schema_editor):
    User = apps.get_model("auth", "User")
    Post = apps.get_model("blog", "Post")
    author, _ = User.objects.get_or_create(username="tigran", defaults={"first_name": "Тигран", "password": make_password("blogpass123")})
    for title, body in POSTS:
        Post.objects.create(title=title, body=body, author=author)


def unseed(apps, schema_editor):
    apps.get_model("blog", "Post").objects.filter(title__in=[p[0] for p in POSTS]).delete()


class Migration(migrations.Migration):
    dependencies = [("blog", "0001_initial"), ("auth", "0012_alter_user_first_name_max_length")]
    operations = [migrations.RunPython(seed, unseed)]
