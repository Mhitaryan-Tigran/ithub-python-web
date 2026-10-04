from flask import Flask, render_template

app = Flask(__name__)

RESUME = {
    "name": "Тигран Мхитарян",
    "role": "Fullstack-разработчик",
    "city": "Ростов-на-Дону",
    "about": "Студент IThub по специальности 09.02.07 «Информационные системы и программирование». Работаю fullstack-разработчиком, в свободное время делаю приложения для macOS.",
    "contacts": [("GitHub", "https://github.com/Mhitaryan-Tigran")],
    "experience": [
        {"place": "leto.link", "role": "Fullstack-разработчик", "period": "сейчас", "points": ["Сеть SEO-сайтов на разных доменах", "Внутренние инструменты команды"]},
    ],
    "projects": [
        {"name": "Skywall", "text": "Живые обои для macOS", "stack": ["Swift", "Metal"]},
        {"name": "SkyNotch", "text": "Плеер в вырезе экрана MacBook с обложкой и волной звука", "stack": ["Swift", "SwiftUI"]},
        {"name": "SkyDuo", "text": "Анимация сгиба рабочего стола при закрытии крышки", "stack": ["Swift"]},
    ],
    "education": [{"place": "IThub college", "speciality": "09.02.07 Информационные системы и программирование", "period": "3 курс"}],
    "skills": {"Языки": ["Python", "JavaScript", "TypeScript", "Swift", "SQL"], "Веб": ["Flask", "Django", "Node.js", "Express"], "Инструменты": ["Git", "Docker", "Linux"]},
}


@app.route("/")
def resume():
    return render_template("resume.html", r=RESUME)


if __name__ == "__main__":
    app.run(debug=True)
