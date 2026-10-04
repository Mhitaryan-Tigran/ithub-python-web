from django.views.generic import TemplateView

RESUME = {
    "name": "Тигран Мхитарян",
    "role": "Fullstack-разработчик",
    "city": "Ростов-на-Дону",
    "about": "Студент IThub по специальности 09.02.07 «Информационные системы и программирование». Работаю fullstack-разработчиком, в свободное время делаю приложения для macOS.",
    "experience": [{"place": "leto.link", "role": "Fullstack-разработчик", "period": "сейчас", "points": ["Сеть SEO-сайтов на разных доменах", "Внутренние инструменты команды"]}],
    "projects": [
        {"name": "Skywall", "text": "Живые обои для macOS", "stack": ["Swift", "Metal"]},
        {"name": "SkyNotch", "text": "Плеер в вырезе экрана MacBook", "stack": ["Swift", "SwiftUI"]},
        {"name": "SkyDuo", "text": "Анимация сгиба рабочего стола при закрытии крышки", "stack": ["Swift"]},
    ],
    "skills": {"Языки": ["Python", "JavaScript", "TypeScript", "Swift", "SQL"], "Веб": ["Django", "Flask", "Node.js"], "Инструменты": ["Git", "Docker", "Linux"]},
}


class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["r"] = RESUME
        return context


class AboutPageView(TemplateView):
    template_name = "about.html"
