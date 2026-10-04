import random

from flask import Flask, render_template

app = Flask(__name__)

QUOTES = [
    ("Жребий брошен.", "Гай Юлий Цезарь"),
    ("Пришёл, увидел, победил.", "Гай Юлий Цезарь"),
    ("Знание — сила.", "Фрэнсис Бэкон"),
    ("Я мыслю, следовательно, существую.", "Рене Декарт"),
    ("Тише едешь — дальше будешь.", "русская пословица"),
]


@app.route("/")
def index():
    text, author = random.choice(QUOTES)
    return render_template("index.html", text=text, author=author)


if __name__ == "__main__":
    app.run(debug=True)
