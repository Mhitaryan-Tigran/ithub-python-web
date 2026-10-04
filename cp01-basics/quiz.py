QUESTIONS = [
    ("Какая функция выводит текст на экран?", ["input()", "print()", "len()"], 2),
    ("Какой тип у значения 3.14?", ["int", "str", "float"], 3),
    ("Как получить длину списка items?", ["len(items)", "items.length", "size(items)"], 1),
    ("Какой оператор возводит в степень?", ["^", "**", "pow"], 2),
    ("Что вернёт 7 // 2?", ["3", "3.5", "4"], 1),
    ("Как начинается комментарий в Python?", ["//", "#", "--"], 2),
    ("Какое ключевое слово объявляет функцию?", ["func", "def", "function"], 2),
    ("Что вернёт 'IThub'.lower()?", ["ITHUB", "ithub", "Ithub"], 2),
    ("Какой цикл повторяется, пока условие истинно?", ["for", "while", "repeat"], 2),
    ("Какое значение у bool('')?", ["True", "False", "None"], 2),
]


def ask(number, question, options):
    print(f"\n{number}. {question}")
    for i, option in enumerate(options, 1):
        print(f"   {i}) {option}")
    while True:
        answer = input("Ваш ответ (1-3): ").strip()
        if answer in ("1", "2", "3"):
            return int(answer)
        print("Введите число 1, 2 или 3")


def main():
    print("Тест по основам Python: 10 вопросов, в каждом 3 варианта ответа.")
    score = 0
    for number, (question, options, right) in enumerate(QUESTIONS, 1):
        if ask(number, question, options) == right:
            print("Правильно")
            score += 1
        else:
            print("Не правильно")
    print(f"\nИтог: {score} из {len(QUESTIONS)}")


if __name__ == "__main__":
    main()
