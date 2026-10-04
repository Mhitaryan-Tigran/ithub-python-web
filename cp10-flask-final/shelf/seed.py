import click

from . import db
from .models import Book, User

READERS = [
    ("Тигран", "tigran@example.com", "Читаю про продукт и дизайн", [
        ("Стив Джобс", "Уолтер Айзексон", "done", 5, "О том, как упрямство и вкус превращаются в продукт."),
        ("Чистый код", "Роберт Мартин", "reading", None, ""),
        ("Дизайн привычных вещей", "Дональд Норман", "want", None, ""),
    ]),
    ("Мария", "maria@example.com", "Классика и фантастика", [
        ("Мастер и Маргарита", "Михаил Булгаков", "done", 5, "Перечитываю каждый год и каждый раз нахожу новое."),
        ("Пикник на обочине", "Аркадий и Борис Стругацкие", "done", 4, "Коротко, страшно и очень по-человечески."),
    ]),
]


@click.command("seed")
def seed_command():
    db.drop_all()
    db.create_all()
    for name, email, about, books in READERS:
        user = User(name=name, email=email, about=about)
        user.set_password("password123")
        db.session.add(user)
        for title, author, status, rating, review in books:
            db.session.add(Book(owner=user, title=title, author=author, status=status, rating=rating, review=review))
    db.session.commit()
    click.echo("Демо-данные созданы: tigran@example.com и maria@example.com, пароль password123")
