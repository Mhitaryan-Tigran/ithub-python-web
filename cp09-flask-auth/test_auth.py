from project import create_app

app = create_app()
app.config.update(TESTING=True, SQLALCHEMY_DATABASE_URI="sqlite:///:memory:")
client = app.test_client()

with app.app_context():
    from project import db
    db.drop_all()
    db.create_all()

assert client.get("/profile").status_code == 302
print("Профиль без входа -> перенаправление на вход")
r = client.post("/signup", data={"email": "test@example.com", "name": "Тест", "password": "secret1"}, follow_redirects=True)
assert "Аккаунт создан" in r.text
print("Регистрация -> аккаунт создан")
r = client.post("/login", data={"email": "test@example.com", "password": "wrong"}, follow_redirects=True)
assert "Проверьте" in r.text
print("Неверный пароль -> ошибка")
r = client.post("/login", data={"email": "test@example.com", "password": "secret1"}, follow_redirects=True)
assert "Добро пожаловать, Тест" in r.text
print("Вход -> профиль: Добро пожаловать, Тест!")
client.get("/logout")
assert client.get("/profile").status_code == 302
print("Выход -> профиль снова закрыт")
print("Все проверки пройдены")
