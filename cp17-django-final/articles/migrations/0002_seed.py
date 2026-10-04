from django.contrib.auth.hashers import make_password
from django.db import migrations

AUTHORS = [("tigran", "Тигран", 18), ("maria", "Мария", 18), ("daniil", "Даниил", 19)]
ARTICLES = [
    ("tigran", "tech", "Как мы сдавали пересдачи и не сошли с ума", "Осень — время пересдач. Главный совет: разбить всё на маленькие задачи и закрывать по одной в день.\n\nСделайте список всех контрольных точек, отметьте, что уже сдано, и начните с того, что ближе по сроку. Работы удобно хранить в репозитории: тогда ничего не потеряется, а преподавателю достаточно отправить ссылку."),
    ("maria", "life", "Студенческий хакатон: 24 часа без сна", "В субботу в колледже прошёл первый хакатон. Двенадцать команд за сутки собрали прототипы — от бота расписания до игры про сессию.\n\nПобедила команда второго курса с сервисом обмена конспектами. Следующий хакатон обещают весной."),
    ("daniil", "study", "Шпаргалка по Django: от модели до страницы", "Модель описывает данные, миграция создаёт таблицу, представление достаёт записи, шаблон их показывает, а urls.py связывает адрес с представлением.\n\nЕсли запомнить эту цепочку, любое приложение на Django читается как книга."),
    ("tigran", "news", "В колледже открылась новая лаборатория", "На третьем этаже заработала лаборатория с новыми компьютерами и большим экраном для защиты проектов.\n\nЗаписаться на свободные часы можно у куратора группы."),
]
COMMENTS = [
    (0, "maria", "Список задач реально спасает, проверено."),
    (0, "daniil", "А я делаю по одной КТ за вечер — тоже работает."),
    (1, "tigran", "Было круто, в следующий раз пойду участником!"),
]


def seed(apps, schema_editor):
    User = apps.get_model("accounts", "CustomUser")
    Article = apps.get_model("articles", "Article")
    Comment = apps.get_model("articles", "Comment")
    users = {u: User.objects.create(username=u, first_name=n, age=a, password=make_password("newspaper123")) for u, n, a in AUTHORS}
    created = [Article.objects.create(author=users[u], section=s, title=t, body=b) for u, s, t, b in reversed(ARTICLES)][::-1]
    for i, u, text in COMMENTS:
        Comment.objects.create(article=created[i], author=users[u], text=text)


def unseed(apps, schema_editor):
    apps.get_model("accounts", "CustomUser").objects.filter(username__in=[a[0] for a in AUTHORS]).delete()


class Migration(migrations.Migration):
    dependencies = [("articles", "0001_initial"), ("accounts", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
