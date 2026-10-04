import datetime

from flask import Flask, render_template

app = Flask(__name__)


def greeting(hour):
    if 6 <= hour < 12:
        return "Доброе утро"
    if 12 <= hour < 18:
        return "Добрый день"
    if 18 <= hour < 24:
        return "Добрый вечер"
    return "Доброй ночи"


@app.route("/")
def index():
    now = datetime.datetime.now()
    return render_template("index.html", greeting=greeting(now.hour), now=now)


@app.route("/blog")
def blog():
    posts = [
        ("Маршруты во Flask", "Декоратор @app.route связывает адрес страницы с функцией, которая её возвращает."),
        ("Шаблоны Jinja2", "Шаблон index.html наследует base.html и заполняет блок content."),
    ]
    return render_template("blog.html", posts=posts)


@app.route("/calendar")
def calendar():
    today = datetime.date.today()
    days = [today + datetime.timedelta(days=i) for i in range(7)]
    return render_template("calendar.html", days=days, today=today)


if __name__ == "__main__":
    assert [greeting(h) for h in (6, 11, 12, 17, 18, 23, 0, 5)] == ["Доброе утро", "Доброе утро", "Добрый день", "Добрый день", "Добрый вечер", "Добрый вечер", "Доброй ночи", "Доброй ночи"]
    app.run(debug=True)
