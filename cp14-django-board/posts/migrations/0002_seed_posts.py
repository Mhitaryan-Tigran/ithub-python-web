from django.db import migrations

ADS = [
    ("Продам учебник по матанализу", "Демидович, сборник задач. Есть пометки карандашом, все страницы на месте.", "sell", 400, "@tigran_m"),
    ("Куплю б/у монитор 24″", "Нужен для второго экрана, IPS, без битых пикселей. Могу забрать сам.", "buy", 6000, "@daniil_b"),
    ("Помогу с Python и Django", "Объясню ORM, представления и шаблоны, разберу ваш код перед сдачей.", "service", 500, "@anna_v"),
    ("Найдены наушники в 301 аудитории", "Белые беспроводные, в чёрном чехле. Опишите их — верну.", "lost", None, "@maria_a"),
    ("Продам механическую клавиатуру", "Свичи Brown, раскладка RU/EN, комплект кейкапов в подарок.", "sell", 3500, "@ilya_g"),
]


def seed(apps, schema_editor):
    Post = apps.get_model("posts", "Post")
    for title, text, category, price, contact in ADS:
        Post.objects.create(title=title, text=text, category=category, price=price, contact=contact)


def unseed(apps, schema_editor):
    apps.get_model("posts", "Post").objects.filter(title__in=[a[0] for a in ADS]).delete()


class Migration(migrations.Migration):
    dependencies = [("posts", "0001_initial")]
    operations = [migrations.RunPython(seed, unseed)]
