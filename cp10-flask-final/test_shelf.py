from shelf import create_app

app = create_app({"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", "TESTING": True})
c = app.test_client()

assert c.get("/").status_code == 200 and c.get("/profile").status_code == 302
print("Главная открыта, полка без входа закрыта")
r = c.post("/signup", data={"name": "Тигран", "email": "t@e.com", "password": "secret1"}, follow_redirects=True)
assert "Добро пожаловать" in r.text
print("Регистрация и автоматический вход")
r = c.post("/books/new", data={"title": "Дюна", "author": "Фрэнк Герберт", "status": "done", "rating": "5", "review": "Песок"}, follow_redirects=True)
assert "Дюна" in r.text
print("Книга добавлена в базу")
r = c.post("/books/1/edit", data={"title": "Дюна", "author": "Фрэнк Герберт", "status": "reading", "rating": ""}, follow_redirects=True)
assert "Читаю" in r.text
print("Статус изменён")
c.get("/logout")
c.post("/signup", data={"name": "Чужой", "email": "x@e.com", "password": "secret1"})
assert c.post("/books/1/delete").status_code == 403
print("Чужую книгу удалить нельзя (403)")
print("Все проверки пройдены")
